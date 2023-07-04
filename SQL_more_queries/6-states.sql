-- Creates database and table States

CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
USE bbtn_0d_usa;

CREATE TABLE IF NOT EXIST states (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
