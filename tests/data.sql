INSERT INTO user (id, username, password)
VALUES
  ("test_user_1", 'test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ("test_user_2", 'other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79'),
  ("rizhiy_user_id", 'rizhiy', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f');

INSERT INTO wish (id, title, desc, rough_price, currency, picture_url, reserved_by)
VALUES
  ("edit_test_wish", 'Edit Test Wish', 'Description for edit test', 50.00, 'USD', 'http://example.com/edit_image.png', NULL);

INSERT INTO wish_link (id, url, desc, wish_id)
VALUES
  ("edit_link1", 'http://example.com/edit', 'Edit Example', "edit_test_wish"),
  ("edit_link2", 'http://example.org/edit', 'Edit Example Org', "edit_test_wish");
