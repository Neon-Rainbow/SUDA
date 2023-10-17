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

--1.��ѯ������19��21��֮���Ů����ѧ��,����,����,������Ӵ�С����
select sno,sname,sage
from student
where ssex = 'Ů' and sage between 19 and 21
order by sage desc;

--2.��ѯ�����е�2����Ϊ�������ֵ�ѧ��ѧ�š��Ա�
select sno,ssex
from student
where sname like '_��%';

--3.��ѯ 1001�γ�û�гɼ���ѧ��ѧ�š��γ̺�
select sno,cno
from sc
where cno = '1001' and grade is null;

--4.��ѯJSJ ��SX��WL ϵ���������25���ѧ��ѧ��,�����������ϵ��ѧ������
select sno,sname
from student
where sdept in ('jsj','sx','wl') and sage>25
order by sdept,sno

--5.��10���Ʋ�ѯѧ����sno,cno,10���Ƴɼ� ��1-10�� Ϊ1 ��11-20��Ϊ2 ��30-39��Ϊ3��������90-100Ϊ10�� 
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

--6.��ѯ student ���е�ѧ�����ֲ����Ǽ���ϵ�С���distinct��
select distinct sdept
from student;

--7.��ѯ0001��ѧ��1001��1002�γ̵ĳɼ���
select grade
from sc
where sno = '0001' and cno in('1001','1002')

