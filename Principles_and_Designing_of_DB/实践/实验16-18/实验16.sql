use school

insert into Student values('0001','张三','男',20,'JSJ')
insert into Student values('0002','李四','女',25,'SX')

-- 一 理解rollback
Select * from student where sno= '0001'

BEGIN TRANsaction
     Update student set sage=sage+1 where sno='0001'
     Select * from student where sno='0002'

Select * from student where sno='0001'

ROLLBACK  TRANsaction

Select * from student where sno= '0001'

-- 二 理解commit
Select * from student where sno='0001'

BEGIN TRANsaction 
     Update student set sage=sage+1 where sno='0001'
     Select * from student where sno='0002'

commit transaction
Select * from student where sno='0001'

BEGIN TRANsaction 
     Update student set sage=sage+1 where sno=’0001’
     Update sc set grade=grade + 1 where sno=’0002’ and cno=’1001’
  Rollback
