--ʵ��һ 
--1.�½����ݿ�school_DB,�ڸ����ݿ���������²�����
create database school_DB

--2.д��ʹ�� Create Table ��䴴���� student , sc,course ��SQL��䡣
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

--3.ʹ�� SP_HELP �鿴�� student �ı�ṹ
exec sp_help 'student'

--4.���� sql ����ṹ�޸�
alter table Student add address varchar(60),inDate date;
alter table Student alter column address varchar(50)
alter table Student drop column inDate

--5.ɾ����
drop table SC
drop table Student
drop table Course
