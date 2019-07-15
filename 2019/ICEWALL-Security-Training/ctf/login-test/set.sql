create user if not exists 'sqluser'@'localhost' identified by 'Passw0rD123';
create database if not exists `mydb`;
grant all privileges on *.* to 'sqluser'@'localhost' identified by 'Passw0rD123';

use mydb;

create table if not exists `FlaG_i5_heRe` (
  flag VARCHAR(32) NOT NULL,
  PRIMARY KEY (flag)
);
create table if not exists `users` (
  id VARCHAR(32) NOT NULL, 
  pw VARCHAR(32) NOT NULL, 
  PRIMARY KEY (id)
);

insert into FlaG_i5_heRe (flag) values ('FLAG{thisistestflag}');
INSERT INTO users (id, pw) VALUES ('admin','flag is not here just in db!');
INSERT INTO users (id, pw) VALUES ('seonguk','babobab0');
INSERT INTO users (id, pw) VALUES ('youngjoong','cheonjaeman!');
INSERT INTO users (id, pw) VALUES ('icewall','world-best club');
