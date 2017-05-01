CREATE DATABASE animals;

\connect animals;

CREATE TABLE dogs (
  id   SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  age  INTEGER NULL
);

INSERT INTO dogs (name, age) VALUES ('fido', 3);
INSERT INTO dogs (name, age) VALUES ('molly', 5);
INSERT INTO dogs (name, age) VALUES ('lassy', 7);
