-- create table id_not_null with id attribute value set to default 1.
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
