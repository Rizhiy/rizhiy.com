from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template(
        "index.html.jinja",
        github="https://github.com/Rizhiy",
        linkedin="https://linkedin.com/in/rizhiy/",
        imdb="https://www.imdb.com/user/ur62161138/ratings/",
        goodreads="https://www.goodreads.com/rizhiy",
        steam="https://steamcommunity.com/id/Rizhiy/",
    )
