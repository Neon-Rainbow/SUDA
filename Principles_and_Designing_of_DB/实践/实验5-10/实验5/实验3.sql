--ʵ���� ��������������
--1.ʵ��������
insert into student values
(3001,'�Դ�','��',20,'SX'),
(3002,'����','Ů',21,'JSJ'),
(3001,'����','Ů',21,'SX');

select * from student;

insert into course values(1081,'��������',null,4);

insert into sc values
(3001,1081,90),
(3001,1081,79);

--2.�û��Զ���������Լ��
insert into student values
('3005','�Դ�','��',14,'SX'),
('3006','����','��',21,'JSJ');
select * from student;

insert into course values
(1085,'C++',null,9),
(1086,'����','1086',3);
select * from course

insert into sc values
(3002,1081,128);
select * from sc

--3.����������Լ��
insert into student values
(4001,'����','��',20,'SX'),
(4002,'�','Ů',20,'JSJ');

insert into course values
(1088,'Java',null,5),
(1089,'��ѧ',null,3)

insert into sc values
(4001,1088,90),
(4002,1088,86)

insert into sc values
(4001,1066,76)

insert into student values
(4003,'�Ի�','��',21,'SX')

delete from student
where sno = '4001' or sno = '4002'

update student
set sno = '4018'
where sno = '4003';

update student
set sno = '4021'
where sno = '4001'

update sc
set sno = '4001'
where sno = '4001' and cno = '1088' and grade = 90;
