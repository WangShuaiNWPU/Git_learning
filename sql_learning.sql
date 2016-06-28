/* set character set utf8;
create database ws_test5 default character set utf8;

use ws_test5;
create table students
(
    id int unsigned not null auto_increment primary key,  
    name char(8) not null,
    sex char(4) not null,
    age tinyint unsigned not null,
    tel char(13) null default "-"
)default charset=utf8;

set character set utf8;
insert into students values(Null,"王刚","男",20,"13811371377");
insert into students(name,sex,age)values("孙丽华","女",21);
insert into students values(null,"郑平","男",30,"15478965486");
insert into students values(null,"王帅","男",24,"18165383565");
insert into students values(null,"杨宁","女",40,"18681851800"); */

/* select name,age from students; */


/* select * from students where age>=24; */

/* select * from students where id <5 and age>20; */

/* update students set tel=default where id=3;

update students set age = age+1; */









