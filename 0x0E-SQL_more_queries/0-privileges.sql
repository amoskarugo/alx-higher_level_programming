-- script that lists all privileges of the MYSQL users
-- user_0d_1 and user_0d_2 on the server(in localhost).

SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- grants for the other user.

SHOW GRANTS FOR 'user_0d_2'@'localhost';
