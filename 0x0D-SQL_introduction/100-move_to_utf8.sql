-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Converts all the following into UTF*:
	-- The database "hbtn_0c_0"
	-- The table "first_table"
	-- Field "name" in "first_table"
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN NAME VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
