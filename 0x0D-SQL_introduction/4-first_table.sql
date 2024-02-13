-- A script creating a table called "first_table" in the current database
-- first_table description:
	-- id INT
	-- name VARCHAR(256)
-- The database name will be passed as an argument of mysql command
-- If first_table already exists, the script should not fail
-- SELECT or SHOW staements are not allowed
CREATE table IF NOT EXISTS first_table(`id` INT, `name` VARCHAR(256));
