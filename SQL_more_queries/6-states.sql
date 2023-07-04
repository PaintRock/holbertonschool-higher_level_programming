-- Creates database and table States

CREATE IF DOES NOT EXIST hbtn_0d_usa;

CREATE IF DOES NOT EXIST table states (id INT NOT NULL AUTO-INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id) UNIQUE, );
