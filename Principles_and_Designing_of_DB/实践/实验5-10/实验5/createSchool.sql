--ʵ���
create database school
--1.д������������Լ���� Create Table �������student��course��sc 
create table Student(
	Sno char(6) not null,
	Sname varchar(8) not null,
	Ssex char(2) not null,
	Sage smallint not null,
	Sdept varchar(15) not null default('JSJ'),
	primary key(Sno),
	unique(Sname),
	check(Ssex in('��','Ů')),
	check(Sage>16),
)

create table Course(
	Cno char(4) not null,
	Cname varchar(20) not null,
	Cpno char(4),
	Ccredit tinyint not null check(ccredit IN (0, 1, 2, 3, 4, 5)),
	primary key(Cno),
	unique(Cno,Cpno)
)

create table SC(
	Sno char(6) not null,
	Cno char(4) not null,
	Grade decimal(12,1) not null,
	constraint PK_SC primary key(Sno,Cno),
	foreign key(sno) references student(sno),
    foreign key(cno) references course(cno)
)

--2.ʹ�� SP_HELP �鿴�� student ����������Լ����������¼��ʹ�� SP_HELP �鿴�� sc ����������������������¼��

exec sp_help 'student'
exec sp_help 'Course'
exec sp_help 'sc'

--3.����alter table ��ӡ�ɾ��������Լ��
alter table sc 
drop constraint PK_SC

alter table sc
drop constraint FK__SC__Cno__0F624AF8

alter table sc
add constraint PK_SC primary key(Sno,Cno)

alter table sc
add foreign key(Cno) references Course(Cno)

alter table sc
add check(grade > 0 and grade < 100)

select * from student
select * from course
select * from sc


drop table SC
drop table Student
drop table Course
