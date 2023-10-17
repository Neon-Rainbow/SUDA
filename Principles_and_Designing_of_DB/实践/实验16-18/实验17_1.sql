use school

BEGIN TRANsaction 
      Update student set sage=sage+1 where sno='0001'
      Select * from student where sno='0002'

select * from  student where sno='0002'

commit Tran

BEGIN TRAN 
        Select * from student where sno='0001'
        Print 'server process ID (spid) :' 
        Print @@spid

exec sp_lock 

commit tran
   exec sp_lock

BEGIN TRAN 
        Update student  set  sage=sage + 1  where sno='1001'
        Print 'server process ID (spid) : '
        Print @@spid

exec sp_lock 

commit tran
   exec sp_lock

SET TRANSACTION ISOLATION LEVEL Serializable

BEGIN TRAN
   Select * from student (TABLOCKX) where sno='1002'
   Print 'Server Process ID (spid): '
   Print @@spid
  
exec sp_lock

set lock_timeout 1000      
go
BEGIN TRAN
   Select * from student (TABLOCKX) where sno='1002'
