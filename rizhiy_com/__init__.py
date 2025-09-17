"""Artem Vasenin's personal website (rizhiy.com)"""

from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from rizhiy_com import auth, index, wishlist
from rizhiy_com.db import init_app


def create_app(test_config=None) -> Flask:
    load_dotenv()
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=Path(app.instance_path) / "rizhiy.sqlite",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    Path(app.instance_path).mkdir(exist_ok=True, parents=True)
    (Path(app.instance_path) / "pictures").mkdir(exist_ok=True)
    init_app(app)

    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(wishlist.bp)
    app.add_url_rule("/", endpoint="index")

    return app


def create_app_for_proxy() -> Flask:
    app = create_app()
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    return app


__version__ = "1.3.0"
