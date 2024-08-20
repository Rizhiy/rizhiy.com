import datetime as dt
import json
from functools import wraps

import requests
from flask import Blueprint, current_app, flash, g, redirect, render_template, request, session, url_for
from oauthlib.oauth2 import WebApplicationClient
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.wrappers.response import Response

from rizhiy_com.db import get_db
from rizhiy_com.utils import get_id

GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
bp = Blueprint("auth", __name__, url_prefix="/auth")


def get_redirect_url_base(request):
    # Just hardcode the base url for now
    return f"{request.scheme}://{current_app.config['CURRENT_URL']}{request.path}"


def login_user(user_id: str) -> Response:
    pre_login = session.get("pre_login")

    session.clear()
    session["user_id"] = user_id
    load_logged_in_user()

    if pre_login:
        pre_login_dt = dt.datetime.fromtimestamp(pre_login["timestamp"])
        if pre_login_dt > dt.datetime.now() - dt.timedelta(minutes=5):
            return redirect(pre_login["url"])

    return redirect(url_for("index"))


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                user_id = get_id()
                db.execute(
                    "INSERT INTO user (id, username, password) VALUES (?, ?, ?)",
                    (user_id, username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return login_user(user_id)

        flash(error, "error")

    return render_template("auth/register.html.jinja")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            return login_user(user["id"])

        flash(error, "error")

    return render_template("auth/login.html.jinja")


@bp.route("/login/google")
def google_login():
    client = WebApplicationClient(current_app.config["GOOGLE_CLIENT_ID"])

    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=f"{get_redirect_url_base(request)}/callback",
        scope=["email"],
    )
    return redirect(request_uri)


@bp.route("/login/google/callback")
def google_login_callback():
    code = request.args.get("code")

    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    client = WebApplicationClient(current_app.config["GOOGLE_CLIENT_ID"])

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=get_redirect_url_base(request),
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(current_app.config["GOOGLE_CLIENT_ID"], current_app.config["GOOGLE_CLIENT_SECRET"]),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    response_json = userinfo_response.json()
    if not response_json.get("email_verified"):
        flash("Google authentication failed!", "error")
        return redirect(url_for("auth.login"))

    user_google_id = userinfo_response.json()["sub"]
    user_email = userinfo_response.json()["email"]
    user_picture_url = userinfo_response.json()["picture"]

    db = get_db()

    user = db.execute("SELECT * FROM user WHERE id = ?", (user_google_id,)).fetchone()
    if not user:
        db.execute(
            "INSERT INTO user (id, username, picture_url) VALUES (?, ?, ?)",
            (user_google_id, user_email, user_picture_url),
        )
        db.commit()
        user = db.execute("SELECT * FROM user WHERE id = ?", (user_google_id,)).fetchone()

    return login_user(user["id"])


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()


@bp.route("/logout")
def logout():
    last_page = session.get("prev_page", ("index", {}))
    session.clear()
    return redirect(url_for(last_page[0], **last_page[1]))


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            session["pre_login"] = {"url": get_redirect_url_base(request), "timestamp": dt.datetime.now().timestamp()}
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.after_app_request
def save_response(r):
    if request.method == "POST" or request.endpoint == "static":
        return r

    session["prev_page"] = (request.endpoint, request.view_args)
    return r
