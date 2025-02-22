from rizhiy_com.db import get_db


def test_add_wish(client, app, auth):
    auth.login(username="rizhiy", password="test")  # noqa: S106
    response = client.post(
        "/wishlist/add",
        data={
            "title": "New Wish",
            "desc": "A new wish description",
            "rough_price": "100.00",
            "currency": "USD",
            "picture_url": "http://example.com/image.png",
            "link_urls": ["http://example.com", "http://example.org"],
            "link_descs": ["Example", "Example Org"],
        },
    )
    assert response.status_code == 200

    with app.app_context():
        db = get_db()
        wish = db.execute("SELECT * FROM wish WHERE title = 'New Wish'").fetchone()
        assert wish["title"] == "New Wish"
        links = db.execute("SELECT * FROM wish_link WHERE wish_id = ?", (wish["id"],)).fetchall()
        assert len(links) == 2
        assert links[0]["url"] == "http://example.com"
        assert links[1]["url"] == "http://example.org"


def test_edit_wish(client, app, auth):
    auth.login(username="rizhiy", password="test")  # noqa: S106
    response = client.post(
        "/wishlist/edit_test_wish/edit",
        data={
            "title": "Updated Wish",
            "desc": "Updated description",
            "rough_price": "150.00",
            "currency": "EUR",
            "picture_url": "http://example.com/new_image.png",
            "link_urls": ["http://example.com/updated", "http://example.org/updated"],
            "link_descs": ["Updated Example", "Updated Example Org"],
        },
    )
    assert response.status_code == 302
    follow_response = client.get(response.headers["Location"])
    assert follow_response.status_code == 200

    with app.app_context():
        db = get_db()
        wish = db.execute("SELECT * FROM wish WHERE id = 'edit_test_wish'").fetchone()
        assert wish["title"] == "Updated Wish"
        links = db.execute("SELECT * FROM wish_link WHERE wish_id = 'edit_test_wish'").fetchall()
        assert len(links) == 2
        assert links[0]["url"] == "http://example.com/updated"
        assert links[1]["url"] == "http://example.org/updated"


def test_edit_wish_non_rizhiy(client, app, auth):
    auth.login()
    response = client.post(
        "/wishlist/edit_test_wish/edit",
        data={
            "title": "Should Not Update",
            "desc": "This should not be updated",
            "rough_price": "200.00",
            "currency": "GBP",
            "picture_url": "http://example.com/should_not_update.png",
            "link_urls": ["http://example.com/should_not_update"],
            "link_descs": ["Should Not Update"],
        },
    )
    assert response.status_code == 403

    with app.app_context():
        db = get_db()
        wish = db.execute("SELECT * FROM wish WHERE id = 'edit_test_wish'").fetchone()
        assert wish["title"] == "Edit Test Wish"  # Ensure the title has not changed
        links = db.execute("SELECT * FROM wish_link WHERE wish_id = 'edit_test_wish'").fetchall()
        assert len(links) == 2
        assert links[0]["url"] == "http://example.com/edit"
        assert links[1]["url"] == "http://example.org/edit"


def test_open_edit_page(client, auth):
    auth.login(username="rizhiy", password="test")  # noqa: S106
    response = client.get("/wishlist/edit_test_wish/edit")
    assert response.status_code == 200


def test_open_edit_page_non_rizhiy(client, auth):
    auth.login()
    response = client.get("/wishlist/edit_test_wish/edit")
    assert response.status_code == 403


def test_open_wishlist_page(client):
    response = client.get("/wishlist/")
    assert response.status_code == 200


def test_reserve_wish(client, auth):
    auth.login()
    response = client.get("/wishlist/edit_test_wish/reserve")
    assert response.status_code == 302  # Expect a redirect after reserving
    follow_response = client.get(response.headers["Location"])
    assert follow_response.status_code == 200

    with client.application.app_context():
        db = get_db()
        wish = db.execute("SELECT * FROM wish WHERE id = 'edit_test_wish'").fetchone()
        assert wish["reserved_by"] == "test_user_1"  # Assuming 'test_user_1' is the logged-in user ID
