CREATE DATABASE IF NOT EXISTS db_login;
USE db_login;
CREATE TABLE IF NOT EXISTS tb_login(id int auto_increment primary key,
                            email varchar(50) not null unique,
                            password varchar(50) not null);