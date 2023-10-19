-- create user 'user_0d_1' if the user does not exist.
-- should have all the privileges.
-- set password to 'user_0d_1_pwd'

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

