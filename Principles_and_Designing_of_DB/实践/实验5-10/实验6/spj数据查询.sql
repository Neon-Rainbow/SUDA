create database SPJ

CREATE TABLE SB (
  SN CHAR(4),
  SNAME VARCHAR(50),
  CITY VARCHAR(50),
  PRIMARY KEY (SN)
);

CREATE TABLE PB (
  PN CHAR(4),
  PNAME VARCHAR(50),
  COLOR VARCHAR(50),
  WEIGHT DECIMAL(10,2),
  PRIMARY KEY (PN)
);

CREATE TABLE JB (
  JN CHAR(4),
  JNAME VARCHAR(50),
  CITY VARCHAR(50),
  PRIMARY KEY (JN)
);

CREATE TABLE SPJB (
  SN CHAR(4),
  PN CHAR(4),
  JN CHAR(4),
  QTY INT,
  PRIMARY KEY (SN, PN, JN, QTY),
  FOREIGN KEY (SN) REFERENCES SB (SN),
  FOREIGN KEY (PN) REFERENCES PB (PN),
  FOREIGN KEY (JN) REFERENCES JB (JN)
);

insert into sb values
('S1','N1','�Ϻ�'),
('S2','N2','����'),
('S3','N3','����'),
('S4','N4','�Ϻ�'),
('S5','N5','�Ͼ�');

insert into pb values
('P1','PN1','��','12'),
('P2','PN2','��','18'),
('P3','PN3','��','20'),
('P4','PN4','��','13'),
('P5','PN5','��','11'),
('P6','PN6','��','15');

insert into jb values
('J1','JN1','�Ϻ�'),
('J2','JN2','����'),
('J3','JN3','�Ͼ�'),
('J4','JN4','�Ͼ�'),
('J5','JN5','�Ϻ�'),
('J6','JN6','�人'),
('J7','JN7','�Ϻ�');

insert into spjb values
('S1','P1','J1',200),
('S1','P1','J4',700),
('S2','P3','J1',400),
('S2','P3','J2',200),
('S2','P3','J3',200),
('S2','P3','J4',500),
('S2','P3','J5',600),
('S2','P3','J6',400),
('S2','P3','J7',800),
('S2','P3','J2',100),
('S3','P3','J1',200),
('S3','P3','J2',500),
('S4','P6','J3',300),
('S4','P6','J7',300),
('S5','P2','J2',200),
('S5','P2','J4',100),
('S5','P5','J5',500),
('S5','P5','J7',100),
('S5','P6','J2',200),
('S5','P1','J4',1000),
('S5','P3','J4',1200),
('S5','P4','J4',800),
('S5','P5','J4',400),
('S5','P6','J4',500);

--1.����Ӧ�̱�����������������SPJB��Ϣ
select *
from spjb
order by sn asc,qty desc;

--2.ȡ��s1��Ӧ�̹�Ӧ�������������С��������������֮�ƽ������
select max(qty) as '�������',min(qty) as '��С����',(max(qty) - min(qty)) as '����֮��',avg(qty) as 'ƽ������'
from spjb
where sn = 's1';

--3.�����Ӧ�̹�Ӧ�����ƽ��������������Ӧ�̺Ž�������
select sn,avg(qty) as 'ƽ������'
from spjb
group by sn
order by sn;

--4.��ѯ��Ӧ�����������800���ϵĹ��̱�ź��乩Ӧ��������
select pn, sum(qty) as '������'
from spjb
group by pn
having sum(qty)>800;

--5.��ѯ���й��̵�ȫ��ϸ��
select *
from jb;

--6.��ѯ���ڳ���Ϊ�Ϻ������й��̵�ȫ��ϸ��
select *
from jb
where city = '�Ϻ�'

--7.��ѯ�ṩ�����������300�Ĺ�Ӧ�̵ı��
select sn
from spjb
group by sn
having sum(qty)>300;

--8.��ѯΪ����J1�ṩ����Ĺ�Ӧ�̴���
select sn
from spjb
where jn = 'J1';

--9.��ѯΪ����J1�ṩ���P1�Ĺ�Ӧ�̴���
select distinct sn
from spjb
where jn = 'J1' and pn = 'P1';

--10.ȡ��Ϊ����J1��J2�ṩ����Ĺ�Ӧ�̴���
select distinct sn
from spjb
where jn in ('J1','J2');

--11.ȡ���ɹ�Ӧ��S1�ṩ����Ĺ��̵Ĵ���
select jn 
from spjb 
where sn='s1' group by jn

--12.ȡ�����������10-20֮��������Ϣ
select *
from pb
where weight between 10 and 20;

--13.ȡ�������ԡ�������ͷ�Ĺ�Ӧ�̵ı�š����ơ�����
select sn,sname,city
from sb 
where city like'��%'
