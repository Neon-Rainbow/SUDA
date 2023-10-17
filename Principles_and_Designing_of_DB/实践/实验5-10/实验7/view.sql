use school
--1.建立学生学号、姓名、性别、课程号、成绩的视图 v_sc
create view v_sc as(
	select s.sno,s.sname,s.ssex,sc.cno,sc.grade
	from student as s join sc on s.sno = sc.sno
);

-- 查看V_sc中的数据
select *
from v_sc

--2.建立学生学号、姓名、出生年份的视图 v_age
create view v_age as(
	select sno,sname,sage
	from student
);

-- 查看V_age中的数据
select *
from v_age

--3.建立 ‘JSJ’ 系的学生学号、姓名、性别、年龄的视图 V_JSJ
create view v_jsj as(
	select sno,sname,ssex,sage
	from student
	where sdept = 'jsj'
);

--4.建立每门课程的平均分的视图 V_avggrade
create view v_avggrade as(
	select cno,avg(grade) as avg_grade
	from sc
	group by cno
);

--5.将 视图 v_jsj 中 李文庆 的年龄改为21岁
update v_jsj
set sage = 21
where sname = '李文庆';

--6.察看 student 中李文庆的年龄
select sage
from student
where sname = '李文庆';

--查看 v_age 中李文庆的出生年月
select sage
from v_jsj
where sno = '李文庆';

--7.查询每门课程的及格率
create view v1 as(
	select cno, count(*) as a
	from sc
	group by cno
)
create view v2 as(
	select cno,count(*) as b
	from sc
	where grade>= 60
	group by cno
) 

select v2.cno,b/a*1.0
from v1 join v2 on v1.cno = v2.cno
