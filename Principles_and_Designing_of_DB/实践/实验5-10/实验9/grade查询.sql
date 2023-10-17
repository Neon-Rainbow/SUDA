--完成以下的SQL查询，将对应的SQL语句写在每道题目的下方
use grade
--1、查询学生的全部信息。
select *
from s;

--2、查询选修了课程的学生号。
select distinct sno
from sc;

--3、查询选修课程号为‘C1’的学生的学号和成绩。
select sno,score
from sc
where cno = 'C1';

--4、查询成绩高于85分的学生的学号、课程号和成绩。
select sno,cno,score
from sc
where score>85;

--5、查询选修C1或C2且分数大于等于85分学生的的学号、课程号和成绩。
select sno,cno,score
from sc
where cno in('C1','C2') and score>85;

--6、查询工资在1000至1500之间的教师的教师号、姓名及职称。
select tno,tn,prof
from t
where sa between 1000 and 1500;

--7、查询没有选修C1，也没有选修C2的学生的学号、课程号和成绩。
select sno, cno, score 
from SC 
where sno not in (
	select sno 
	from SC 
	where cno in ('c1','c2'));

--8、查询所有姓张的教师的教师号和姓名。
select tno,tn
from t
where tn like '张%';

--9、查询姓名中第二个汉字是“力”的教师号和姓名。
select tno,tn
from t
where tn like '_力%';

--10、查询没有考试成绩的学生的学号和相应的课程号。
select sno,cno
from sc
where score is null;

--11、查询选修C1 的学生学号和成绩，并按成绩降序排列。
select sno,score
from sc
where cno = 'c1'
order by score desc;

--12、查询选修C1、C2的学号、课程号和成绩，查询结果按学号升序排列，学号相同再按成绩降序排列。
select sno,cno,score
from sc
where cno in ('c1','c2')
order by sno,score desc;

--13. 求学号为S1学生的总分和平均分。
select max(score) as max_score,avg(score) as avg_score
from sc
where sno = 's1'；

--14、求选修C1号课程的最高分、最低分及之间相差的分数
select max(score),min(score),max(score)-min(score)
from sc
where cno = 'C1';

--15、求计算机系学生的总数
select count(*)
from s join dep on s.DEPtid = dep.DEPtid
where depname = '计算机系';

--16、查询各位教师的教师号及其任课的门数。
select tno,count(distinct cno)
from tc 
group by tno;

--17、查询选修两门以上课程的学生学号和选课门数
select sno,count(distinct cno)
from sc
group by sno
having count(distinct sno)>2;

--18、求选课在三门以上且各门课程均及格的学生的学号及其总成绩，查询结果按总成绩降序列出。
select sno,sum(score)
from sc
group by sno
having count(distinct cno)>3 and min(score)>=60
order by sum(score);

--19、查询与刘明教师职称相同的教师号、姓名。
select t1.tno,t1.tn
from t as t1,t as t2
where t1.prof = t2.prof and t2.tn = '刘明' and t1.tno != t2.tno

--20、查询讲授课程号为C1的教师姓名。
select tn
from t join tc on t.tno=tc.tno
where cno = 'C1';

--21、查询讲授课程号为C1的教师姓名，系名和课程名。
select tn,deptid,cname
from t,tc,course
where t.tno = tc.tno and course.cno = tc.cno and tc.cno = 'c1'

--22、查询计算机系的学生选修课程的课程名、学号、成绩
select course.cname,s.sno,sc.score
from course,s,sc,dep
where course.cno = sc.cno and sc.sno = s.sno and dep.DEPtid = s.DEPtid and dep.DEPname = '计算机系'

--23、查询‘王立’选修的课程名。 
select cname
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and s.sname = '王立';

--24、查询‘王立’选修的课程名和成绩。
select cname,score
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and s.sname = '王立';

--25、查询'王立'的总分、平均分
select sum(score) as '总分', avg(score) as '平均分'
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and s.sname = '王立';

--26、显示学生姓名及该学生的平均分
select sname,avg(score) as '平均分'
from s join sc on s.sno = sc.sno
group by s.sname;

--27、显示学生学号、学生姓名及该学生的平均分
select s.sno,sname,avg(score) as '平均分'
from s join sc on s.sno = sc.sno
group by s.sno,sname;

--28、查询每一门课的间接先修课（即先修课的先修课）
select c1.cname as '课程名',c2.cname '先修课程名'
from course as c1,course as c2
where c1.pcno = c2.cno;

--29、查询选修c1号课程且成绩在70分以上的所有学生的详细信息
select s.sno,sname,age,deptid
from s join sc on s.sno = sc.sno
where sc.cno = 'c1' and score > 70;

--30.  查询与“王立”在同一个系学习的学生姓名
select s1.sname
from s as s1,s as s2
where s2.Sname = '王立' and s1.sno != s2.Sno and s1.DEPtid = s2.DEPtid;

--31.查询选修了课程名为“计算机原理”的学生学号和姓名
select s.sno,sname 
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and cname = '计算机原理';

--32.查询其他系中比计算机系所有学生年龄都小的学生姓名及年龄。
with min_age_cmop(min_age) as(
	select min(age)
	from s,dep
	where s.DEPtid = dep.DEPtid and dep.DEPname = '计算机系'
)
select sname,age
from s,dep,min_age_cmop
where s.DEPtid = dep.DEPtid and dep.DEPname != '计算机系' and s.age < min_age; 

--33.查询没有选课的学生的姓名
select sname
from s left outer join sc on s.sno = sc.Sno
where cno IS NULL;

--34.找出成绩高于所有选修课程平均成绩的学号和成绩。
with avg_score(value) as(
	select avg(score)
	from sc
)
select s.sno,sc.score
from s,sc,avg_score
where s.sno = sc.sno and sc.score > avg_score.value;

--35、查询其他系中比计算机系所有教师工资都高的教师的姓名和工资。
with max_salary(salary) as(
	select max(sa)
	from t join dep on t.DEPtid = dep.DEPtid
	where depname = '计算机系'
)
select tn,sa
from t,dep,max_salary
where t.DEPtid = DEP.DEPtid and DEP.DEPname = '计算机系' and t.SA > max_salary.salary

--36.检索至少选修了刘伟老师所授课程中一门课程的学生姓名；
with liuwei_class(cno) as(
	select cno
	from t join tc on t.tno = tc.tno
	where t.tn = '刘伟'
) 
select sname
from s,sc,liuwei_class
where sc.sno = s.sno and sc.cno = liuwei_class.cno;

--37.检索李楠同学不学的课程的课程号
select distinct sc.cno
from sc
except
select distinct sc.cno
from sc join s on sc.sno = s.sno
where s.sname = '李楠'

--20.求没有选修”数据库原理”课程的学生的姓名。
select sname 
from s 
where sno not in (
	select sno 
	from sc,course 
	where sc.cno=course.cno and course.cname='数据库原理'
)

--38.查询计算机系的学生与年龄不大于19岁的学生的交集
select s.sno
from s join dep on s.DEPtid = dep.DEPtid
where dep.DEPname = '计算机系'
intersect
select sno
from s
where age<=19

--39.查询选修课程c1的学生集合与选修课程c2的学生集合的交集
select sno 
from sc 
where cno='c1' 
intersect 
select sno 
from sc 
where cno='c2'

--40.查询计算机系的学生与年龄不大于19岁的学生的差集。
select s.sno
from s join dep on s.DEPtid = dep.DEPtid
where dep.DEPname = '计算机系'
except
select sno
from s
where age<=19