create database grade

create table DEP(
    DEPtid char(10) not null,
    DEPname char(10) not null,
    DEPzr char(10) not null,
    
    primary key(DEPtid)
)

create table S(
    Sno char(10) not null,
    Sname char(10) not null,
    age int default(20),
    DEPtid char(10) not null,

    primary key(Sno),
    unique(Sname)
)

create table Course(
    Cno char(10) not null,
    Cname char(10) not null,
    PCno char(10),

    primary key(Cno),
    unique(Cno,PCno)
)

create table SC(
    Sno char(10) not null,
    Cno char(10) not null,
    score int check(score < 100 and score > 0),

    primary key(Sno,Cno),
    foreign key(Sno) references S(Sno),
    foreign key(Cno) references Course(Cno)
)

create table T(
    Tno char(10) not null,
    Tn char(10) not null,
    PROF char(10) not null,
    SA DECIMAL(10, 2) not null,
    DEPtid char(10),

    primary key(Tno),
    foreign key(DEPtid) references DEP(DEPtid),
    check(SA >= 1000)
)

create table TC(
	TNO char(10) not null,
	CNO char(10) not null,
	book char(10),

	primary key(TNO,CNO),
	foreign key(TNO) references T(tno),
	foreign key(cno) references Course(cno)

)

insert into dep (deptid, depname, depzr) values
  (01, '�����ϵ', '����'),
  (02, '��Ϣ����ϵ', '����');

insert into s (sno, sname, age, deptid) values
  ('s1', '����', 16, 01),
  ('s2', '���', 18, 02);

insert into course(cno, cname, pcno) values
  ('c1', '�����ԭ��', null),
  ('c2', '���繤��', 'c1'),
  ('c3', '���ݿ�ԭ��', 'c2');

insert into sc (sno, cno, score) values
  ('s1', 'c1', 88),
  ('s1', 'c2', 70),
  ('s2', 'c1', null),
  ('s2', 'c2', 56),
  ('s1', 'c3', 89);

insert into t (tno, tn, prof, sa, deptid) values
  ('t1', '����', '��ʦ', 1800.00, 01),
  ('t2', '����', '����', 1200.00, 02),
  ('t3', '��ΰ', '������', 2000.00, null),
  ('t4', '����', '����', 1000.00, null);

insert into tc (tno, cno, book) values
  ('t1', 'c1', '�����ԭ��'),
  ('t2', 'c2', '���繤��'),
  ('t3', 'c1', '�����ԭ��'),
  ('t4', 'c2', '���繤��');

alter table S
add constraint fk_s foreign key(DEPtid) references DEP(deptid)

alter table t
add constraint d_t default '������' for PROF

alter table s
add inDate date
exec sp_help s

alter table s
drop column inDate

alter table t
drop constraint d_t

