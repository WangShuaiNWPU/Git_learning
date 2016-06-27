create database ws_test2 character set utf8;

use ws_test2;
create table students
(
    id int unsigned not null auto_increment primary key,  
    name char(8) not null,
    sex char(4) not null,
    age tinyint unsigned not null,
    tel char(13) null default "-"
);

insert into students values(Null,"王刚","男",20,"13811371377");

insert into students(name,sex,age)values("孙丽华","女",21);

/* select name,age from students; */