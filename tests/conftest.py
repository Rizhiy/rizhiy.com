import os
import tempfile
from pathlib import Path

import pytest

from rizhiy_com import create_app
from rizhiy_com.db import get_db, init_db

_data_sql = (Path(__file__).parent / "data.sql").read_bytes().decode("utf8")


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app(
        {
            "TESTING": True,
            "DATABASE": db_path,
            "SECRET_KEY": "testing",
            "RIZHIY_ID": "rizhiy_user_id",
            "CURRENT_URL": "localhost",
        },
    )

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)  # noqa: PTH108


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):  # noqa: S107
        return self._client.post(
            "/auth/login",
            data={"username": username, "password": password},
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)
