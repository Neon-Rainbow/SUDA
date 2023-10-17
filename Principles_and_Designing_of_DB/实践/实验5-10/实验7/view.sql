use school
--1.����ѧ��ѧ�š��������Ա𡢿γ̺š��ɼ�����ͼ v_sc
create view v_sc as(
	select s.sno,s.sname,s.ssex,sc.cno,sc.grade
	from student as s join sc on s.sno = sc.sno
);

-- �鿴V_sc�е�����
select *
from v_sc

--2.����ѧ��ѧ�š�������������ݵ���ͼ v_age
create view v_age as(
	select sno,sname,sage
	from student
);

-- �鿴V_age�е�����
select *
from v_age

--3.���� ��JSJ�� ϵ��ѧ��ѧ�š��������Ա��������ͼ V_JSJ
create view v_jsj as(
	select sno,sname,ssex,sage
	from student
	where sdept = 'jsj'
);

--4.����ÿ�ſγ̵�ƽ���ֵ���ͼ V_avggrade
create view v_avggrade as(
	select cno,avg(grade) as avg_grade
	from sc
	group by cno
);

--5.�� ��ͼ v_jsj �� ������ �������Ϊ21��
update v_jsj
set sage = 21
where sname = '������';

--6.�쿴 student �������������
select sage
from student
where sname = '������';

--�鿴 v_age ��������ĳ�������
select sage
from v_jsj
where sno = '������';

--7.��ѯÿ�ſγ̵ļ�����
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
