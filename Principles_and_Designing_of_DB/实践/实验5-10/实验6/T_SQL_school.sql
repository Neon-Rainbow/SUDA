--第三部分：统计
use school
--1查询姓名中有“明”字的学生人数。
select count(sno) as '人数'
from student
where sname = '%明%';
--2计算‘JSJ’系的平均年龄及最大年龄。
select avg(sage),max(sage)
from student
where sdept = 'jsj';
--3查询学生中姓名为张明、赵英的人数
select count(sno)
from student
where sname in ('张明','赵英');
--4计算每一门课的总分、平均分，最高分、最低分，按平均分由高到低排列
select cno,sum(grade),avg(grade),max(grade),min(grade) 
from sc
group by cno 
order by avg(grade) desc
--5 计算 1001,1002 课程的平均分。
select cno , avg(grade) 
from sc
where cno in ('1001','1002') Group by cno
--6 查询平均分大于80分的学生学号及平均分 
select sno,avg(grade)
from sc
where grade>80;
--7 统计选修课程超过 2 门的学生学号
select sno
from sc
group by sno
having count(*)>2;
--8 统计有10位成绩大于85分以上的课程号。
select distinct cno
from sc
where grade>85
group by cno
having count(*) > 10;
--9 统计平均分不及格的学生学号
select distinct sno
from sc
group by sno
having avg(grade)<60;
--10 统计有大于两门课不及格的学生学号
select sno 
from sc
where grade<60 
group by sno 
having count(*) >2

--第四部分：连接

--1查询 JSJ 系的学生选修的课程号
select distinct cno
from student join sc on student.sno = sc.sno
where sdept = 'jsj';

--2查询选修1002 课程的学生的学生姓名 (不用嵌套及嵌套2种方法）
select sname
from student join sc on student.sno = sc.sno
where cno = '1002'

select sname
from student
where sno in(
	select sno
	from sc
	where cno = '1002'
);

--3查询数据库原理不及格的学生学号及成绩
select sno,grade
from course join sc on course.cno = sc.cno
where  cname = '数据库原理' and grade<60;
--4查询选修“数据库原理”课且成绩 80 以上的学生姓名(不用嵌套及嵌套2种方法）
select sname
from student,sc,course
where student.sno = sc.sno and sc.cno = course.cno and cname = '数据库原理' and grade > 80;

select sname
from student
where sno in(
	select sno
	from sc
	where cno in(
		select cno
		from course
		where cname = '数据库原理'
	)
);
--5查询平均分不及格的学生的学号，姓名,平均分。
select sc.sno,sname,avg(grade)
from student join sc on student.sno = sc.sno
group by sc.sno
having avg(grade)<60;
--6查询女学生平均分高于75分的学生姓名。
select sname
from student join sc on student.sno = sc.sno
where ssex = '女'
group by student.sno
having avg(grade) > 75;
--7查询男学生学号、姓名、课程号、成绩。(一门课程也没有选修的男学生也要列出，不能遗漏)
select student.sno,sname,cno,grade
from student left outer join sc on student.sno = sc.sno
where student.ssex = '男';

--第五部分：嵌套、相关及其他

--一.在school数据库中完成以下查询：
--1 查询平均分不及格的学生人数
select count(*)
from sc
group by sno
having avg(grade)<60
--2 查询没有选修1002 课程的学生的学生姓名
select sname
from student
where sno not in(
	select sno
	from sc
	where cno = '1002'
);
--3 查询平均分最高的学生学号及平均分 （2种方法 TOP , any , all）
select top 1 sno,avg(grade)
from sc
group by sno
order by avg(grade) desc;

select sno,avg(grade)
from sc
where avg(grade)>= all(
	select avg(grade)
	from sc
	group by sno
);

--*4 查询没有选修1001，1002课程的学生姓名
select sname
from student
where sno not in(
	select sno
	from sc
	where cno in('1001','1002')
);
--5 查询1002课程第一名的学生学号（2种方法）
select top 1 sno
from sc
where cno = '1002'
order by grade desc;

with max_grade(value) as(
	select max(grade)
	from sc
)
select sno
from sc,max_grade
where grade = max_grade.value
--6 查询平均分前三名的学生学号
select top 3 sno
from sc
group by avg(grade);
--7 查询 JSJ 系的学生与年龄不大于19岁的学生的差集
select *
from student
where sdept = 'jsj'
except
select *
from student
where sage<19;
--8 查询1001号课程大于90分的学生学号、姓名及平均分大于85分的学生学号、姓名
with avg_grade_greater_85(sno) as(
	select sno
	from sc
	group by sno
	having avg(grade) > 85
)
select sc.sno,student.sname
from sc,avg_grade_greater_85,student
where sc.sno = avg_grade_greater_85.sno and sc.sno = student.sno and cno = '1001' and grade>90; 
--9 查询每门课程成绩都高于该门课程平均分的学生学号
with avg_grade(grade) as(
	select avg(grade)
	from sc
	group by sno
)
select sno
from sc,avg_grade
where sc.grade > avg_grade.grade;
--10查询大于本系科平均年龄的学生姓名
with avg_age(age) as(
	select avg(sage)
	from student
)
select sname
from student,avg_age
where student.sage > avg_age.age;

