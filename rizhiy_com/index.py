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
        bgg="https://boardgamegeek.com/collection/user/Rizhiy",
        steam="https://steamcommunity.com/id/Rizhiy/",
        mal="https://myanimelist.net/animelist/rizhiy",
    )
