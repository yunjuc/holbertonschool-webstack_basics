-- create a table with default id field and not null
CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1 NOT NULL,
name VARCHAR(256)
);
