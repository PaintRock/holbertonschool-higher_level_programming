-- this is a statement

CREATE USER IF NOT EXISTS '{username}'@'localhost' IDENTIFIED BY '{password}';
GRANT ALL PRIVILEGES ON *.* TO '{username}'@'localhost' WITH GRANT OPTION;
