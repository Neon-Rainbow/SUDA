use grade

--1
insert into s values
('s7','郑东',21,01);

--2
insert into SC values
('s7','c1',null);

--3
create table avgsal(
    department char(10),
    avg_sa int
);
insert into avgsal
select DEP.depname,avg(sa) as '平均工资'
from DEP join T on dep.DEPtid = T.DEPtid
group by DEP.DEPtid,dep.depname

--4
update T
set DEPtid = (
    select DEPtid
    from DEP
    where DEPname = '信息管理系'
    )
where Tn = '刘伟';

--5
update S
set age = age + 1;

--6
update t
set SA = SA * 1.2
where SA<=1000 and PROF = '讲师';

--7
update t
set SA = SA + 1000
where SA < (
    select avg(sa)
    from t
    );

--8
update t
set sa = sa + 100
where tno in (
    select TNO
    from TC
    where cno = 'c5'
    );

--9、把所有教师的工资提高到平均工资的1.2倍
update t
set sa = 1.2 * (
    select avg(sa)
    from t
    );
--10、将刘伟教师的工资置为空值
update t
set sa = null
where tn = '刘伟';
--11、删除刘伟教师授课的记录。
delete from tc
where TNO in (
    select TNO
    from T
    where Tn = '刘伟'
    );
