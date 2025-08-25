import logging
import math
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Blueprint, current_app, flash, g, redirect, render_template, request, send_from_directory, url_for
from PIL import Image
from replete import split_list
from werkzeug.exceptions import abort
from werkzeug.wrappers.request import Request
from werkzeug.wrappers.response import Response

from rizhiy_com.auth import login_required
from rizhiy_com.db import get_db
from rizhiy_com.utils import HEADERS, get_exchange_rate, get_id, get_url_title

LOGGER = logging.getLogger(__name__)

SAVED_IMG_PREFIX = "processed://"
SAVED_IMG_PREFIX_LEN = len(SAVED_IMG_PREFIX)
SAVED_IMG_SIZE = 256, 256
MAX_RESERVE = 3

bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")


def check_is_rizhiy() -> None:
    if g.user["id"] != current_app.config["RIZHIY_ID"]:
        abort(403, "Only rizhiy can edit wishes!")


def get_wish(wish_id: str) -> dict[str, Any]:
    db = get_db()
    query = db.execute("SELECT * FROM wish WHERE id = ?", (wish_id,))
    columns = [d[0] for d in query.description]
    wish = dict(zip(columns, query.fetchone(), strict=False))
    wish["links"] = db.execute("SELECT * FROM wish_link WHERE wish_id = ?", (wish_id,)).fetchall()
    return wish


@bp.route("/")
def index():
    db = get_db()
    query = db.execute("SELECT * FROM wish")
    columns = [d[0] for d in query.description]
    wishes = [dict(zip(columns, r, strict=False)) for r in query.fetchall()]

    for wish in wishes:
        if isinstance(wish["rough_price"], int | float):
            try:
                wish["usd_price"] = wish["rough_price"] * get_exchange_rate(wish["currency"])
            except Exception:
                LOGGER.exception(f"Couldn't get exchange rate for {wish['currency']}")
                wish["usd_price"] = None

        if wish["picture_url"].startswith(SAVED_IMG_PREFIX):
            wish["picture_url"] = url_for("wishlist.serve_picture", path=wish["picture_url"][SAVED_IMG_PREFIX_LEN:])

        wish["links"] = db.execute("SELECT * FROM wish_link WHERE wish_id = ?", (wish["id"],)).fetchall()
    for wish in wishes:
        if wish.get("usd_price"):
            wish["usd_price"] = math.ceil(wish["usd_price"])
    available, all_reserved = split_list(wishes, lambda w: w["reserved_by"] is None)
    wishes = []

    user_reserved = []
    if g.user:
        user_reserved = list(filter(lambda w: w["reserved_by"] == g.user["id"], all_reserved))
    for reserved in user_reserved:
        all_reserved.remove(reserved)
    wishes.extend(user_reserved)

    available = sorted(available, key=lambda w: w.get("usd_price") or 0)
    wishes.extend(available)
    wishes.extend(all_reserved)

    return render_template("wishlist/index.html.jinja", wishes=wishes)


def insert_or_update(request: Request, id_: str = None) -> Response:
    title = request.form["title"]
    if not title:
        flash("Title is required!", "error")
        redirect(url_for("wishlist.add"))

    id_ = id_ or get_id()

    db = get_db()
    fields = ["desc", "rough_price", "currency", "picture_url"]
    # TODO: Need to download the image and save locally
    db.execute(
        f"INSERT OR REPLACE INTO wish (id, title, {', '.join(fields)}, reserved_by) VALUES (?, ?, ?, ?, ?, ?, NULL)",  # noqa: S608
        (id_, title, *(request.form[field] for field in fields)),
    )
    link_urls = request.form.getlist("link_urls") or []
    link_descs = request.form.getlist("link_descs") or []

    db.execute("DELETE FROM wish_link WHERE wish_id = ?", (id_,))
    for url, desc in zip(link_urls, link_descs, strict=False):
        url = url.strip()
        desc = desc or get_url_title(url)
        if url:
            link_id = get_id()
            db.execute(
                "INSERT INTO wish_link (id, url, desc, wish_id) VALUES (?, ?, ?, ?)",
                (link_id, url, desc, id_),
            )
    db.commit()

    save_wish_img(id_)

    return redirect(url_for("wishlist.index"))


@bp.route("/add", methods=("GET", "POST"))
@login_required
def add():
    check_is_rizhiy()

    if request.method == "POST":
        insert_or_update(request)

    return render_template("wishlist/add.html.jinja")


@bp.route("/<id_>/edit", methods=("GET", "POST"))
@login_required
def edit(id_):
    check_is_rizhiy()

    wish = get_wish(id_)
    if not wish:
        flash("Invalid wish id provided", "error")
        return redirect(url_for("wishlist.index"))

    if request.method == "POST":
        return insert_or_update(request, id_)
    return render_template("wishlist/edit.html.jinja", wish=wish)


@bp.route("/<id_>/reserve", methods=("GET",))
@login_required
def reserve(id_):
    wish = get_wish(id_)
    if wish["reserved_by"] and g.user["id"] != wish["reserved_by"]:
        flash("This wish is already reserved by someone else", "error")
        return redirect(url_for("wishlist.index"))

    db = get_db()

    new_reserved_user = None if wish["reserved_by"] else g.user["id"]
    num_reserved_wishes = 0

    if new_reserved_user:
        num_reserved_wishes = db.execute("SELECT COUNT(*) FROM wish WHERE reserved_by = ?", (g.user["id"],)).fetchone()[
            0
        ]
        if num_reserved_wishes >= MAX_RESERVE:
            flash(f"Sorry, you can't reserve more than {MAX_RESERVE} wishes", "error")
            return redirect(url_for("wishlist.index"))
        status = "reserved"
    else:
        status = "un-reserved"

    db.execute("UPDATE wish SET reserved_by = ? WHERE id = ?", (new_reserved_user, id_))
    db.commit()
    success_msg = f"You have successfully {status} {wish['title']}"
    if new_reserved_user:
        reserve_remaining = MAX_RESERVE - 1 - num_reserved_wishes
        if reserve_remaining:
            success_msg += f"\nYou can reserve {MAX_RESERVE - num_reserved_wishes - 1} more wishes"
        else:
            flash("You can't reserve any more wishes!", "warning")
    flash(success_msg, "message")
    return redirect(url_for("wishlist.index"))


@bp.route("/<id_>/delete", methods=("POST",))
@login_required
def delete(id_):
    check_is_rizhiy()

    db = get_db()
    db.execute("DELETE FROM wish WHERE id = ?", (id_,))
    db.commit()
    return redirect(url_for("wishlist.index"))


def save_wish_img(wish_id: str) -> None:
    db = get_db()
    img_url = db.execute("SELECT picture_url FROM wish WHERE id = ?", (wish_id,)).fetchone()[0]
    if not img_url or img_url.startswith(SAVED_IMG_PREFIX):
        return

    tmp_dir = Path("/tmp") / "images-for-resize"  # noqa: S108
    tmp_dir.mkdir(exist_ok=True)
    tmp_path = tmp_dir / Path(urlparse(img_url).path).name

    tmp_path.write_bytes(requests.get(img_url, headers=HEADERS).content)

    pictures_dir = Path(current_app.instance_path) / "pictures"
    save_path = pictures_dir / f"{uuid4()}{tmp_path.suffix}"
    save_path.parent.mkdir(exist_ok=True, parents=True)
    with Image.open(tmp_path) as img:
        img.thumbnail(SAVED_IMG_SIZE)
        img.save(save_path)

    db_path = f"{SAVED_IMG_PREFIX}{save_path.relative_to(pictures_dir)}"
    db.execute("UPDATE wish SET picture_url = ? WHERE id = ?", (db_path, wish_id))
    db.commit()


@bp.route("/pictures/<path:path>")
def serve_picture(path):
    # Using request args for path will expose you to directory traversal attacks
    return send_from_directory(Path(current_app.instance_path) / "pictures", path)
