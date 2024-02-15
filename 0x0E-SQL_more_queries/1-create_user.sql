-- Script that creates the MySQL server user 'user_0d_1'
-- The user should have privileges on the server
-- The user password should be set to another user 'user_0d_1_pwd'
-- If user exists, the script should not fail
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
