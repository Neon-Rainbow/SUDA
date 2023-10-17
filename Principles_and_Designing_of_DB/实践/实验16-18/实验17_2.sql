use school

select * from student where sno='0001'

update student set sname='aaa' where sno='0002'

DBCC opentran

select * from  student where sno='0001'

select * from student

set lock_timeout  10000      
go
select * from student
