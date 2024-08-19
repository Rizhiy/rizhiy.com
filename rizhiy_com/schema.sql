DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id VARCHAR(36) PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password VARCHAR(256),
  picture_url TEXT
);

CREATE TABLE wish (
  id VARCHAR(36) PRIMARY KEY,
  title TEXT NOT NULL,
  desc TEXT,
  rough_price DECIMAL(8, 2),
  currency VARCHAR(3),
  picture_url TEXT,
  reserved_by VARCHAR(36),
  FOREIGN KEY (reserved_by) REFERENCES user (id)
);

CREATE TABLE wish_link (
  id VARCHAR(36) PRIMARY KEY,
  url TEXT NOT NULL,
  desc TEXT,
  wish_id VARCHAR(36),
  FOREIGN KEY (wish_id) REFERENCES wish (id)
);
