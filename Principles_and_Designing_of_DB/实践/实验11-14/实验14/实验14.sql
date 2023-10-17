use school
--一.建立学生表的触发器 usp_addstudent，当增加学生时，SX系的学生不能超过30岁
--1.写出触发器
create trigger usp_addstudent on Student
after insert
    as
    begin
        if exists(select 1 from inserted where Sdept = 'SX' and sage >= 30)
        begin
            raiserror('数学系的学生不能超过三十岁',11,1)
            rollback
        end
    end;
--2.执行下列语句块
begin tran
insert into student (sno,sname,ssex,sage,sdept)
values ('0701','刘欢','男',26,'SX')
if @@error=0
  commit
else
  rollback
--3.执行下列语句块
begin tran
insert into student (sno,sname,ssex,sage,sdept)
values ('0702','赵欢','男',31,'SX')
if @@error=0
  commit
else
  rollback

--二.实现下列触发器
--1.不能删除年龄大于25岁的学生记录
create trigger usp_nodelstudent on Student
for delete
    as
    begin
        if exists(select 1 from inserted where sage>25)
        begin
            raiserror('不能删除年龄大于大于25岁的学生记录',11,2)
            rollback
        end
    end;

--2.建立触发器 usp_delcourse , 使课程表中1001，1002，1003 三门课不会被删除。
create trigger usp_delcourse on Course
for delete
    as
    begin
        if exists(select 1 from deleted where cno in ('1001','1002','1003'))
        begin
            raiserror('课程表中1001，1002，1003 三门课不会被删除',11,3)
            rollback
        end
    end;

--3.对学生表建立一触发器，使更改后的年龄只能比原值大
create trigger usp_updateage on Student
after update
    as
    begin
        if exists(
            select 1
            from inserted as i join deleted as d on i.Sno = d.Sno
            where i.Sage < d.Sage
        )
        begin
            raiserror('更改后的年龄只能比原值大',11,4);
            rollback
        end
    end;

--4.对sc表建立触发器，使‘JSJ’系的学生不可选择 ‘1004’号课程
create trigger usp_sccheck on sc
after insert
    as
    begin
        if exists(
            select 1
            from inserted
            where Sdept = 'JSJ' and cno = '1004'
        )
        begin
            raiserror('‘JSJ’系的学生不可选择 ‘1004’号课程',11,5)
            rollback
        end
    end;

--5.对表 course 建触发器，实现级联删除的功能，但某课选修人数大于3则不能删除

--三.建立一个触发器，使对sc表成绩的修改自动记录修改日志
create table tablog (
    用户名 varchar(50),
    学号 varchar(50),
    课程号 varchar(50),
    原成绩 int,
    修改后成绩 int,
    更改日期 datetime
);

create trigger utr_sclog on sc
after update
    as
    begin
        insert into tablog
        select suser_name(),d.sno,d.cno,d.grade,i.grade,getdate()
        from inserted as i join deleted as d on i.sno = d.sno and i.cno = d.cno
    end;

--四.在School数据库中建立一个试验用的发票表bill，然后为发票bill建立触发器 utr_money ,实现当输入单价和数量后，自动填写金额，即发票金额不输入，由单价、数量相乘后自动填写到金额中
create table bill (
    billid char(8),  --发票编号
    date datetime,    --开票日期
    product char(10), --产品编号
    price int,        --单价
    qty int,          --数量
    charge int,       --金额
    primary key (billid)
);

create trigger utr_money on bill
after insert ,update
    as
    begin
        update bill
        set charge = bill.price * bill.qty
        from bill join inserted as i on bill.billid = i.billid
    end;
