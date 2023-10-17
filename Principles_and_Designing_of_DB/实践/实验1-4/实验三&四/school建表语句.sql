create database school

use school

create table Student(
	Sno char(6) not null,
	Sname varchar(8) not null,
	Ssex char(2) not null,
	Sage smallint not null,
	Sdept varchar(15) default('JSJ'),
	primary key(Sno),
	unique(Sname),
	check(Ssex in('男','女')),
	check(Sage>16),
)

create table Course(
	Cno char(6) not null,
	Cname varchar(20) not null,
	Cpno char(4),
	Ccredit tinyint not null check(ccredit IN (0, 1, 2, 3, 4, 5)),
	primary key(Cno),
	unique(Cno,Cpno)
)

create table SC(
	Sno char(6) not null,
	Cno char(6) not null,
	Grade decimal(12,1) not null,
	constraint PK_SC primary key(Sno,Cno),
	foreign key(sno) references student(sno),
    foreign key(cno) references course(cno)
)

INSERT INTO student
VALUES
  (5001, '赵强', '男', 22, 'SX'),
  (5002, '杨丽华', '女', 21, 'JSJ'),
  (5003, '李静', '女', 22, 'SX');

INSERT INTO course
VALUES
  (1801, 'C语言', NULL, 4),
  (1802, '数据结构', 1081, 4);

INSERT INTO SC 
VALUES
  ('5001', 1801, 90),
  ('5001', 1802, 81),
  ('5002', 1801, 91);


