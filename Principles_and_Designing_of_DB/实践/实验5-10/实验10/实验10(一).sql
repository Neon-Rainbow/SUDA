use school
--一.insert
--1.写出把下述学生的信息添加到student表中的命令
insert into student values
(4001,'赵茵','男',20,'SX'),
(4002,'杨华','女',21,null);


--2.批量插入数据
create table sc_name(
    sno char(6),
    sname varchar(8),
    ssex char(2),
    cno char(6),
    grade int
)

insert into sc_name
select student.sno,sname,ssex,cno,grade
from Student join sc on student.sno = sc.Cno and Sdept = 'SX';

select *
from sc_name;

--二.Update
update Student
set sdept = 'JSJ'
where Sno = '0001';

update Student
set Sage = Sage + 1, Ssex = '女'
where sname = '陈小明';

update sc
set Grade = 93
where sno in (
    select sno
    from Student
    where sname = '李文庆'
    );

update sc_name
set grade = grade - 1
where cno in(
    select cno
    from Course
    where cname = '数据库原理'
    );

--三.Delete
delete from Student
where Sdept = 'JSJ';

delete from sc_name
where cno in(
    select cno
    from Course
    where cname = '数据库原理'
    )
