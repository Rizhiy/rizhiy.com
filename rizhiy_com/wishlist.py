import numbers
from contextlib import redirect_stdout
from sqlite3 import Row

from flask import Blueprint, current_app, flash, g, redirect, render_template, request, url_for
from replete import split_list
from werkzeug.exceptions import abort
from werkzeug.wrappers.request import Request
from werkzeug.wrappers.response import Response

from rizhiy_com.auth import login_required
from rizhiy_com.db import get_db
from rizhiy_com.utils import get_exchange_rate, get_id, get_url_title

bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")


def check_is_rizhiy() -> None:
    if g.user["id"] != current_app.config["RIZHIY_ID"]:
        abort(403, "Only rizhiy can edit wishes!")


@bp.route("/")
def index():
    db = get_db()
    query = db.execute("SELECT * FROM wish")
    columns = [d[0] for d in query.description]
    wishes = [dict(zip(columns, r, strict=False)) for r in query.fetchall()]

    for wish in wishes:
        if isinstance(wish["rough_price"], int | float):
            wish["usd_price"] = wish["rough_price"] * get_exchange_rate(wish["currency"])
        else:
            wish["usd_price"] = 0.0
    for wish in wishes:
        wish["usd_price"] = f"{wish['usd_price']:.2f}"
    available, reserved = split_list(wishes, lambda w: w["reserved_by"] is None)
    wishes = []

    user_reserved = next(filter(lambda w: w["reserved_by"] == g.user["id"], reserved), None)
    if user_reserved:
        reserved.remove(user_reserved)
        wishes.append(user_reserved)

    available = sorted(available, key=lambda w: float(w["usd_price"]), reverse=True)
    wishes.extend(available)
    wishes.extend(reserved)

    return render_template("wishlist/index.html.jinja", wishes=wishes)


def insert_or_update(request: Request, id_: str = None) -> Response:
    title = request.form["title"]
    if not title:
        flash("Title is required!")
        redirect(url_for("wishlist.add"))

    id_ = id_ or get_id()

    db = get_db()
    fields = ["desc", "rough_price", "currency", "picture_url"]
    # TODO: Need to download the image and save locally
    db.execute(
        f"INSERT OR REPLACE INTO wish (id, title, {', '.join(fields)}, reserved_by) VALUES (?, ?, ?, ?, ?, ?, NULL)",  # noqa: S608
        (id_, title, *(request.form[field] for field in fields)),
    )
    for link in request.form.get("links", "").splitlines():
        link = link.strip()
        link_text = get_url_title(link)
        link_id = get_id()
        db.execute(
            "INSERT INTO wish_link (id, url, desc, wish_id) VALUES (?, ?, ?)",
            (link_id, link, link_text, id_),
        )
    db.commit()

    return redirect(url_for("wishlist.index"))


@bp.route("/add", methods=("GET", "POST"))
@login_required
def add():
    check_is_rizhiy()

    if request.method == "POST":
        insert_or_update(request)

    return render_template("wishlist/add.html.jinja")


def get_wish(id_: str) -> Row:
    db = get_db()
    wish = db.execute("SELECT * FROM wish WHERE id = ?", (id_)).fetchone()
    if not wish:
        flash("Invalid wish id provided")
        return redirect(url_for("wishlist.index"))


@bp.route("/<id_>/edit", methods=("GET", "POST"))
@login_required
def edit(id_):
    check_is_rizhiy()

    db = get_db()
    wish = db.execute("SELECT * FROM wish WHERE id = ?", (id_)).fetchone()
    if not wish:
        flash("Invalid wish id provided")
        return redirect(url_for("wishlist.index"))

    if request.method == "POST":
        return insert_or_update(request, id_)
    return render_template("wishlist/edit.html.jinja", wish=wish)


@bp.route("/<id_>/reserve", methods=("GET",))
@login_required
def reserve(id_):
    db = get_db()

    wish = db.execute("SELECT reserved_by FROM wish WHERE id = ?", (id_,)).fetchone()
    if wish["reserved_by"] and g.user["id"] != wish["reserved_by"]:
        flash("This wish is already reserved by someone else")
        return redirect(url_for("wishlist.index"))

    new_reserved_user = None if wish["reserved_by"] else g.user["id"]

    if new_reserved_user:
        num_reserved_wishes = db.execute("SELECT COUNT(*) FROM wish WHERE reserved_by = ?", (g.user["id"],)).fetchone()[
            0
        ]
        if num_reserved_wishes > 0:
            flash("Sorry, you can't reserve any more wishes")
            return redirect(url_for("wishlist.index"))

    db.execute("UPDATE wish SET reserved_by = ? WHERE id = ?", (new_reserved_user, id_))
    db.commit()
    return redirect(url_for("wishlist.index"))


@bp.route("/<id_>/delete", methods=("POST",))
@login_required
def delete(id_):
    check_is_rizhiy()

    db = get_db()
    db.execute("DELETE FROM wish WHERE id = ?", (id_,))
    db.commit()
    return redirect(url_for("wishlist.index"))
