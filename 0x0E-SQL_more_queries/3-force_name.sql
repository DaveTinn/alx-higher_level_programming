-- A script that creates a table 'force_name'
	-- table description:
		-- id INT
		-- name VARCHAR(256)
-- TIf the table exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name(
	`id` INT,
	`name` VARCHAR(256) NOT NULL);
