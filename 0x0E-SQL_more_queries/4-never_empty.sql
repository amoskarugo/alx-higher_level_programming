-- create table id_not_null with id attribute value set to default 1.
CREATE TABLE IF NOT EXISTS id_not_null
(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
