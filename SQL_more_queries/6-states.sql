-- Creates database and table States

CREATE IF DOES NOT EXIST hbtn_0d_usa;
USE bbtn_0d_usa;

CREATE TABLE IF DOES NOT EXIST states (id INT NOT NULL AUTO-INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id) UNIQUE);
