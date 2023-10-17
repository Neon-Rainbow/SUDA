--�������֣�ͳ��
use school
--1��ѯ�������С������ֵ�ѧ��������
select count(sno) as '����'
from student
where sname = '%��%';
--2���㡮JSJ��ϵ��ƽ�����估������䡣
select avg(sage),max(sage)
from student
where sdept = 'jsj';
--3��ѯѧ��������Ϊ��������Ӣ������
select count(sno)
from student
where sname in ('����','��Ӣ');
--4����ÿһ�ſε��ܷ֡�ƽ���֣���߷֡���ͷ֣���ƽ�����ɸߵ�������
select cno,sum(grade),avg(grade),max(grade),min(grade) 
from sc
group by cno 
order by avg(grade) desc
--5 ���� 1001,1002 �γ̵�ƽ���֡�
select cno , avg(grade) 
from sc
where cno in ('1001','1002') Group by cno
--6 ��ѯƽ���ִ���80�ֵ�ѧ��ѧ�ż�ƽ���� 
select sno,avg(grade)
from sc
where grade>80;
--7 ͳ��ѡ�޿γ̳��� 2 �ŵ�ѧ��ѧ��
select sno
from sc
group by sno
having count(*)>2;
--8 ͳ����10λ�ɼ�����85�����ϵĿγ̺š�
select distinct cno
from sc
where grade>85
group by cno
having count(*) > 10;
--9 ͳ��ƽ���ֲ������ѧ��ѧ��
select distinct sno
from sc
group by sno
having avg(grade)<60;
--10 ͳ���д������ſβ������ѧ��ѧ��
select sno 
from sc
where grade<60 
group by sno 
having count(*) >2

--���Ĳ��֣�����

--1��ѯ JSJ ϵ��ѧ��ѡ�޵Ŀγ̺�
select distinct cno
from student join sc on student.sno = sc.sno
where sdept = 'jsj';

--2��ѯѡ��1002 �γ̵�ѧ����ѧ������ (����Ƕ�׼�Ƕ��2�ַ�����
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

--3��ѯ���ݿ�ԭ�������ѧ��ѧ�ż��ɼ�
select sno,grade
from course join sc on course.cno = sc.cno
where  cname = '���ݿ�ԭ��' and grade<60;
--4��ѯѡ�ޡ����ݿ�ԭ�����ҳɼ� 80 ���ϵ�ѧ������(����Ƕ�׼�Ƕ��2�ַ�����
select sname
from student,sc,course
where student.sno = sc.sno and sc.cno = course.cno and cname = '���ݿ�ԭ��' and grade > 80;

select sname
from student
where sno in(
	select sno
	from sc
	where cno in(
		select cno
		from course
		where cname = '���ݿ�ԭ��'
	)
);
--5��ѯƽ���ֲ������ѧ����ѧ�ţ�����,ƽ���֡�
select sc.sno,sname,avg(grade)
from student join sc on student.sno = sc.sno
group by sc.sno
having avg(grade)<60;
--6��ѯŮѧ��ƽ���ָ���75�ֵ�ѧ��������
select sname
from student join sc on student.sno = sc.sno
where ssex = 'Ů'
group by student.sno
having avg(grade) > 75;
--7��ѯ��ѧ��ѧ�š��������γ̺š��ɼ���(һ�ſγ�Ҳû��ѡ�޵���ѧ��ҲҪ�г���������©)
select student.sno,sname,cno,grade
from student left outer join sc on student.sno = sc.sno
where student.ssex = '��';

--���岿�֣�Ƕ�ס���ؼ�����

--һ.��school���ݿ���������²�ѯ��
--1 ��ѯƽ���ֲ������ѧ������
select count(*)
from sc
group by sno
having avg(grade)<60
--2 ��ѯû��ѡ��1002 �γ̵�ѧ����ѧ������
select sname
from student
where sno not in(
	select sno
	from sc
	where cno = '1002'
);
--3 ��ѯƽ������ߵ�ѧ��ѧ�ż�ƽ���� ��2�ַ��� TOP , any , all��
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

--*4 ��ѯû��ѡ��1001��1002�γ̵�ѧ������
select sname
from student
where sno not in(
	select sno
	from sc
	where cno in('1001','1002')
);
--5 ��ѯ1002�γ̵�һ����ѧ��ѧ�ţ�2�ַ�����
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
--6 ��ѯƽ����ǰ������ѧ��ѧ��
select top 3 sno
from sc
group by avg(grade);
--7 ��ѯ JSJ ϵ��ѧ�������䲻����19���ѧ���Ĳ
select *
from student
where sdept = 'jsj'
except
select *
from student
where sage<19;
--8 ��ѯ1001�ſγ̴���90�ֵ�ѧ��ѧ�š�������ƽ���ִ���85�ֵ�ѧ��ѧ�š�����
with avg_grade_greater_85(sno) as(
	select sno
	from sc
	group by sno
	having avg(grade) > 85
)
select sc.sno,student.sname
from sc,avg_grade_greater_85,student
where sc.sno = avg_grade_greater_85.sno and sc.sno = student.sno and cno = '1001' and grade>90; 
--9 ��ѯÿ�ſγ̳ɼ������ڸ��ſγ�ƽ���ֵ�ѧ��ѧ��
with avg_grade(grade) as(
	select avg(grade)
	from sc
	group by sno
)
select sno
from sc,avg_grade
where sc.grade > avg_grade.grade;
--10��ѯ���ڱ�ϵ��ƽ�������ѧ������
with avg_age(age) as(
	select avg(sage)
	from student
)
select sname
from student,avg_age
where student.sage > avg_age.age;

