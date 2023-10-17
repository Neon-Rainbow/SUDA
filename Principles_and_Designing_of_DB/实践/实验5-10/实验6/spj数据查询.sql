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
('S1','N1','上海'),
('S2','N2','北京'),
('S3','N3','北京'),
('S4','N4','上海'),
('S5','N5','南京');

insert into pb values
('P1','PN1','红','12'),
('P2','PN2','绿','18'),
('P3','PN3','蓝','20'),
('P4','PN4','红','13'),
('P5','PN5','蓝','11'),
('P6','PN6','绿','15');

insert into jb values
('J1','JN1','上海'),
('J2','JN2','广州'),
('J3','JN3','南京'),
('J4','JN4','南京'),
('J5','JN5','上海'),
('J6','JN6','武汉'),
('J7','JN7','上海');

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

--1.按供应商编号升序、数量降序输出SPJB信息
select *
from spjb
order by sn asc,qty desc;

--2.取出s1供应商供应的最大数量、最小数量、及其两者之差，平均数量
select max(qty) as '最大数量',min(qty) as '最小数量',(max(qty) - min(qty)) as '两者之差',avg(qty) as '平均数量'
from spjb
where sn = 's1';

--3.求各供应商供应零件的平均数量，并按供应商号降序排序
select sn,avg(qty) as '平均数量'
from spjb
group by sn
order by sn;

--4.查询供应零件总数量在800以上的工程编号和其供应的总数量
select pn, sum(qty) as '总数量'
from spjb
group by pn
having sum(qty)>800;

--5.查询所有工程的全部细节
select *
from jb;

--6.查询所在城市为上海的所有工程的全部细节
select *
from jb
where city = '上海'

--7.查询提供零件数量大于300的供应商的编号
select sn
from spjb
group by sn
having sum(qty)>300;

--8.查询为工程J1提供零件的供应商代号
select sn
from spjb
where jn = 'J1';

--9.查询为工程J1提供零件P1的供应商代号
select distinct sn
from spjb
where jn = 'J1' and pn = 'P1';

--10.取出为工程J1或J2提供零件的供应商代号
select distinct sn
from spjb
where jn in ('J1','J2');

--11.取出由供应商S1提供零件的工程的代号
select jn 
from spjb 
where sn='s1' group by jn

--12.取出零件重量在10-20之间的零件信息
select *
from pb
where weight between 10 and 20;

--13.取出城市以“北”开头的供应商的编号、名称、城市
select sn,sname,city
from sb 
where city like'北%'
