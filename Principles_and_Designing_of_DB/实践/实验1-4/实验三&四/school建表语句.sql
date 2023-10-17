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
	check(Ssex in('��','Ů')),
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
  (5001, '��ǿ', '��', 22, 'SX'),
  (5002, '������', 'Ů', 21, 'JSJ'),
  (5003, '�', 'Ů', 22, 'SX');

INSERT INTO course
VALUES
  (1801, 'C����', NULL, 4),
  (1802, '���ݽṹ', 1081, 4);

INSERT INTO SC 
VALUES
  ('5001', 1801, 90),
  ('5001', 1802, 81),
  ('5002', 1801, 91);


