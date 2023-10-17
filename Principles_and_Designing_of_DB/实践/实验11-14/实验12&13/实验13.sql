use school

--1.编写一个存储过程 usp_avgage , 向客户端返回每个系科的学生平均年龄
go
create procedure usp_avgage
as
begin
    select Sdept,avg(Sage) as '平均年龄'
    from Student
    group by Sdept
end;

--2.编写一个存储过程 usp_sdept, 传入一个系科代码，返回该系的平均年龄，人数
go
create procedure usp_sdept
    @sdept varchar(15)
as
begin
    select avg(sage),count(*)
    from Student
    where Sdept = @sdept;
end;

--3.编写存储过程 usp_updateGrade , 传入参数为课程号
go
create procedure usp_updateGrade
    @cno char(4)
as
    begin
        update sc
        set Grade = case
            when grade>80 then Grade + 2
            when grade>60 then Grade + 1
            else Grade - 1
        end
        where cno = @cno;

        select sno,grade
        from sc
        where cno = @cno;
    end;

--4.编写存储过程 usp_g1 , 传入参数课程号，对该门课程进行如下处理
go
create procedure usp_g1
    @cno char(4)
as
    begin
        declare @avg_grade decimal(12,1)
        select @avg_grade = avg(grade)
        from sc
        where cno = @cno;

        update sc
        set grade = case
            when Grade < @avg_grade - 5 then grade
            when Grade < @avg_grade then Grade + 1
            when Grade < @avg_grade then Grade + 1
            when Grade < @avg_grade then Grade + 2
        end
        where cno = @cno
    end;

--5.编写存储过程  usp_comp_age , 比较0001，0002学生的年龄的高低
go
create procedure usp_comp_age
    @sno1 char(4),
    @sno2 char(4)
as
    begin
        declare @age1 int,@age2 int
        select @age1 = Sage
        from Student
        where sno = @sno1;

        select @age2 = Sage
        from Student
        where sno = @sno2;

        if @age1 > @age2
            select sname + '学生的年龄大' as 结果
            from Student
            where sno = @sno1;
        else if @age2 > @age1
            select sname + '学生的年龄大' as 结果
            from Student
            where sno = @sno2;
        else
            select '两个学生的年龄相同' as '结果';
    end;

--6
go
CREATE PROCEDURE usp_comp
    @Cno1 char(4),
    @Cno2 char(4)
AS
BEGIN
    DECLARE @AvgGrade1 decimal(12, 1), @AvgGrade2 decimal(12, 1);
    SELECT @AvgGrade1 = AVG(Grade)
    FROM SC
    WHERE Cno = @Cno1;

    SELECT @AvgGrade2 = AVG(Grade)
    FROM SC
    WHERE Cno = @Cno2;

    IF @AvgGrade1 > @AvgGrade2
        SELECT Cname + '课程的平均分高' AS '结果'
        FROM Course
        WHERE Cno = @Cno1;
    ELSE IF @AvgGrade1 < @AvgGrade2
        SELECT Cname + '课程的平均分高' AS '结果'
        FROM Course
        WHERE Cno = @Cno2;
    ELSE
        SELECT '两门课程的平均分相同' AS '结果';
END;

--7
go
create procedure usp_comp_age1
    @sno1 char(4),
    @sno2 char(4)
as
    begin
        declare @age1 int,@age2 int
        select @age1 = Sage
        from Student
        where sno = @sno1;

        select @age2 = Sage
        from Student
        where sno = @sno2;

        if @age1 > @age2
            select sname + '学生的年龄大' as 结果
            from Student
            where sno = @sno1;
        else if @age2 > @age1
            select sname + '学生的年龄大' as 结果
            from Student
            where sno = @sno2;
        else
            select '两个学生的年龄相同' as '结果';
    end;

--8
exec usp_comp_age1 '0002','0003';

--9
go
CREATE PROCEDURE usp_comp1
    @Cno1 char(4),
    @Cno2 char(4)
AS
BEGIN
    DECLARE @AvgGrade1 decimal(12, 1), @AvgGrade2 decimal(12, 1);
    SELECT @AvgGrade1 = AVG(Grade)
    FROM SC
    WHERE Cno = @Cno1;

    SELECT @AvgGrade2 = AVG(Grade)
    FROM SC
    WHERE Cno = @Cno2;

    IF @AvgGrade1 > @AvgGrade2
        SELECT Cname + '课程的平均分高' AS '结果'
        FROM Course
        WHERE Cno = @Cno1;
    ELSE IF @AvgGrade1 < @AvgGrade2
        SELECT Cname + '课程的平均分高' AS '结果'
        FROM Course
        WHERE Cno = @Cno2;
    ELSE
        SELECT '两门课程的平均分相同' AS '结果';
END;

--10
go
create procedure usp_comp_age2
    @sno1 char(4),
    @sno2 char(4)
as
    begin
        declare @age1 int,@age2 int
        select @age1 = Sage
        from Student
        where sno = @sno1;

        select @age2 = Sage
        from Student
        where sno = @sno2;

        if @age1 > @age2
            select sname,Ssex
            from Student
            where sno = @sno1;
        else if @age2 > @age1
            select sname,Ssex
            from Student
            where sno = @sno2;
        else
            select '两个学生的年龄相同' as '结果';
    end;

--11
go
CREATE PROCEDURE usp_comp2
    @Cno1 char(4),
    @Cno2 char(4)
AS
BEGIN
    DECLARE @AvgGrade1 decimal(12, 1), @AvgGrade2 decimal(12, 1);
    SELECT @AvgGrade1 = AVG(Grade)
    FROM SC
    WHERE Cno = @Cno1;

    SELECT @AvgGrade2 = AVG(Grade)
    FROM SC
    WHERE Cno = @Cno2;

    IF @AvgGrade1 > @AvgGrade2
        SELECT Cname
        FROM Course
        WHERE Cno = @Cno1;
    ELSE IF @AvgGrade1 < @AvgGrade2
        SELECT Cname
        FROM Course
        WHERE Cno = @Cno2;
    ELSE
        SELECT '两门课程的平均分相同' AS '结果';
END;

--12
go
create procedure usp_t1
    @sno char(4)
as
    begin
        declare @grade decimal(12,1);
        select grade
        from sc
        where Sno = @sno and cno = '1001';

        while @grade > 58
        begin
            set @grade = @grade - 1;
            update SC
            set Grade = @grade
            where sno = @sno and cno = '1001';
        end
    end;

--13
go
create procedure usp_t2
    @sdept varchar(15)
as
    begin
        declare @age int;
        set @age = (
            select max(Sage)
            from Student
            where Sdept = @sdept
            );

        while @age < 28
        begin
            update Student
            set sage = Sage + 1
            where Sdept = @sdept;

            set @age = (
            select max(Sage)
            from Student
            where Sdept = @sdept
            );
        end
    end;

--15
go
create procedure usp_disp
    @cno char(4)
as
    begin
        select sno,cno,grade,
            case
                when grade >= 90 then '优'
                when grade >= 80 then '良'
                when grade >= 70 then '中'
                when grade >= 60 then '及格'
                else '不及格'
            end as '等第'
        from SC
        where cno = @cno
    end;

--16
go
create procedure usp_display_grade
    @sno char(6)
as
begin
    select s.sno,s.sname,
        (select sc.grade from sc where cno = '1001') as '1001课程',
        (select sc.grade from sc where cno = '1002') as '1002课程',
        (select sc.grade from sc where cno = '1003') as '1003课程',
        avg(grade)
    from Student as s join sc on s.sno = sc.Sno
    where SC.Sno = @sno
    group by s.sno,s.sname
end;

exec usp_display_grade '5001';

--17
go
create procedure usp_display_grade2
    @sdept varchar(15)
as
begin
    select s.sno,s.sname,
        (select sc.grade from sc where cno = '1001') as '1001课程',
        (select sc.grade from sc where cno = '1002') as '1002课程',
        (select sc.grade from sc where cno = '1003') as '1003课程',
        avg(grade)
    from Student as s join sc on s.sno = sc.Sno
    where Sdept = @sdept
    group by s.sno,s.sname
end;

--18
go
create procedure usp_count_gender_courses
as
begin
    select '男' as '性别',
    sum(case when s.ssex = '男' and sc.cno = '1001' then 1 else 0 end) as '1001人数',
    sum(case when s.ssex = '男' and sc.cno = '1002' then 1 else 0 end) as '1002人数',
    sum(case when s.ssex = '男' and sc.cno = '1001' then 1 else 0 end) as '1003人数',
    sum(case when s.ssex = '男' then 1 else 0 end) as '小计'
    from Student as s join sc on s.sno = sc.sno
    union all
    select '女' as '性别',
    sum(case when s.ssex = '女' and sc.cno = '1001' then 1 else 0 end) as '1001人数',
    sum(case when s.ssex = '女' and sc.cno = '1002' then 1 else 0 end) as '1002人数',
    sum(case when s.ssex = '女' and sc.cno = '1001' then 1 else 0 end) as '1003人数',
    sum(case when s.ssex = '女' then 1 else 0 end) as '小计'
    from Student as s join sc on s.sno = sc.sno
    union all
    select '合计' as '性别',
    sum(case when sc.cno = '1001' then 1 else 0 end) as '1001人数',
    sum(case when sc.cno = '1002' then 1 else 0 end) as '1002人数',
    sum(case when sc.cno = '1003' then 1 else 0 end) as '1003人数',
    count(*) as '小计'
    from SC
end

--19
go
create procedure usp_getDateTime
    @currentDateTime datetime output
as
begin
    set @currentDateTime = getDate();
end

DECLARE @dateTime DATETIME;
EXEC usp_getDateTime @currentDateTime = @dateTime OUTPUT;
SELECT @dateTime AS CurrentDateTime;