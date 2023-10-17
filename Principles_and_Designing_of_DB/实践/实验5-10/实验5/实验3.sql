--实验三 数据完整性试验
--1.实体完整性
insert into student values
(3001,'赵达','男',20,'SX'),
(3002,'杨丽','女',21,'JSJ'),
(3001,'李寅','女',21,'SX');

select * from student;

insert into course values(1081,'电子商务',null,4);

insert into sc values
(3001,1081,90),
(3001,1081,79);

--2.用户自定义完整性约束
insert into student values
('3005','赵达','男',14,'SX'),
('3006','杨丽','南',21,'JSJ');
select * from student;

insert into course values
(1085,'C++',null,9),
(1086,'语文','1086',3);
select * from course

insert into sc values
(3002,1081,128);
select * from sc

--3.参照完整性约束
insert into student values
(4001,'赵尹','男',20,'SX'),
(4002,'杨开','女',20,'JSJ');

insert into course values
(1088,'Java',null,5),
(1089,'数学',null,3)

insert into sc values
(4001,1088,90),
(4002,1088,86)

insert into sc values
(4001,1066,76)

insert into student values
(4003,'赵辉','男',21,'SX')

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
