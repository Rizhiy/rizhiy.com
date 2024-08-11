"""Artem Vasenin's personal website (rizhiy.com)"""

import os
from pathlib import Path

from flask import Flask

from rizhiy_com import auth, blog
from rizhiy_com.db import init_app


def create_app(test_config=None):
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
    init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint="index")

    return app


__version__ = "0.1.0"
