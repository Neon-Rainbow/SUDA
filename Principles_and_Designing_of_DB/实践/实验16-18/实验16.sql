use school

insert into Student values('0001','����','��',20,'JSJ')
insert into Student values('0002','����','Ů',25,'SX')

-- һ ���rollback
Select * from student where sno= '0001'

BEGIN TRANsaction
     Update student set sage=sage+1 where sno='0001'
     Select * from student where sno='0002'

Select * from student where sno='0001'

ROLLBACK  TRANsaction

Select * from student where sno= '0001'

-- �� ���commit
Select * from student where sno='0001'

BEGIN TRANsaction 
     Update student set sage=sage+1 where sno='0001'
     Select * from student where sno='0002'

commit transaction
Select * from student where sno='0001'

BEGIN TRANsaction 
     Update student set sage=sage+1 where sno=��0001��
     Update sc set grade=grade + 1 where sno=��0002�� and cno=��1001��
  Rollback
