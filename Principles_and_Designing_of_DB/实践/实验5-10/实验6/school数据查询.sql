create database school

drop database school

CREATE TABLE student (
  Sno CHAR(6),
  Sname VARCHAR(8),
  Ssex CHAR(2),
  Sage SMALLINT,
  Sdept VARCHAR(15),
  PRIMARY KEY (Sno)
);

CREATE TABLE course (
  Cno CHAR(6),
  Cname VARCHAR(20),
  Cpno CHAR(4),
  Ccredit TINYINT,
  PRIMARY KEY (Cno)
);

CREATE TABLE SC (
  Sno CHAR(6),
  Cno CHAR(6),
  Grade DECIMAL(12,2),
  PRIMARY KEY (Sno, Cno),
  FOREIGN KEY (Sno) REFERENCES student (Sno),
  FOREIGN KEY (Cno) REFERENCES course (Cno)
);

--1.查询年龄在19至21岁之间的女生的学号,姓名,年龄,按年龄从大到小排列
select sno,sname,sage
from student
where ssex = '女' and sage between 19 and 21
order by sage desc;

--2.查询姓名中第2个字为“明”字的学生学号、性别
select sno,ssex
from student
where sname like '_明%';

--3.查询 1001课程没有成绩的学生学号、课程号
select sno,cno
from sc
where cno = '1001' and grade is null;

--4.查询JSJ 、SX、WL 系的年龄大于25岁的学生学号,姓名，结果按系及学号排列
select sno,sname
from student
where sdept in ('jsj','sx','wl') and sage>25
order by sdept,sno

--5.按10分制查询学生的sno,cno,10分制成绩 （1-10分 为1 ，11-20分为2 ，30-39分为3，。。。90-100为10） 
select sno,cno,
case
	when grade between 1 and 10 then 1
	when grade between 11 and 20 then 2
	when grade between 21 and 30 then 3
	when grade between 31 and 40 then 4
	when grade between 41 and 50 then 5
	when grade between 51 and 60 then 6
	when grade between 61 and 70 then 7
	when grade between 71 and 80 then 8
	when grade between 81 and 90 then 9
	when grade between 91 and 100 then 10
end as grade_10
from sc;

--6.查询 student 表中的学生共分布在那几个系中。（distinct）
select distinct sdept
from student;

--7.查询0001号学生1001，1002课程的成绩。
select grade
from sc
where sno = '0001' and cno in('1001','1002')

