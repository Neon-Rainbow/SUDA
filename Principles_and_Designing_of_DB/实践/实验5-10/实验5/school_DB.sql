--实验一 
--1.新建数据库school_DB,在该数据库中完成以下操作：
create database school_DB

--2.写出使用 Create Table 语句创建表 student , sc,course 的SQL语句。
create table Student(
	Sno char(6) not null,
	Sname varchar(8) not null,
	Ssex char(2) not null,
	Sage smallint not null,
	Sdept varchar(15) not null
)

create table Course(
	Cno char(4) not null,
	Cname varchar(20) not null,
	Cpno char(4) not null,
	Ccredit tinyint not null
)

create table SC(
	Sno char(6) not null,
	Cno char(4) not null,
	Grade decimal(12,1) not null
)

--3.使用 SP_HELP 查看表 student 的表结构
exec sp_help 'student'

--4.利用 sql 语句表结构修改
alter table Student add address varchar(60),inDate date;
alter table Student alter column address varchar(50)
alter table Student drop column inDate

--5.删除表
drop table SC
drop table Student
drop table Course
