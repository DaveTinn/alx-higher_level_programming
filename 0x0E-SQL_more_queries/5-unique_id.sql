-- Creates teh table 'unique_id' on MySQL server
	-- table description:
		-- id INT with the default value 1 and must be unique
		-- name VARCHAR(256)
-- Script should not fail if table already exists
CREATE TABLE IF NOT EXISTS unique_id(
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256));
