--创建数据库
create database 书店管理系统

use 书店管理系统

--创建表
create table 书店库存(
	图书编号 nchar(10) primary key,
	书本类别 nchar(10) not null,
	书本数量 int not null,
)

create table 书本信息(
	图书编号 nchar(10) foreign key references 书店库存(图书编号),
	书本类别 nchar(10) not null,
	书本名称 nchar(10) not null,
	书本页数 int not null,
	书本出版商 nchar(10) not null,
	书本价格 float not null,
)

create table 顾客信息(
	顾客卡号 nchar(10) not null primary key,
	顾客姓名 nchar(10) not null,
	顾客性别 nchar(10) not null check(顾客性别 in('男','女')),
	顾客联系方式 nchar(20) not null,
	顾客年龄 int not null,
)

create table 销售信息(
	销售单号 nchar(10) not null primary key,
	图书编号 nchar(10) not null foreign key references 书店库存(图书编号),
	顾客卡号 nchar(10) not null foreign key references 顾客信息(顾客卡号),
	销售数量 int not null,
	销售日期 date default(getdate()),
	销售金额 float default(0),
)

create table 供应商信息(
	供货商号   nchar(10) not null primary key,
	供货商名称 nchar(10) not null,
	供货商电话 nchar(10) not null,
	供货商地址 nchar(10) not null,
)

create table 进货信息(
	进货单号 nchar(10) not null primary key,
	图书编号 nchar(10) not null foreign key references 书店库存(图书编号),
	书本类别 nchar(10) not null,
	供应商号 nchar(10) not null foreign key references 供应商信息(供货商号),
	进货数量 int not null,
	进货日期 date default(getdate())
)

--存储过程
--库存变化的存储过程
go
create procedure 库存变化
	@date1 date,
	@date2 date
as
begin
	select * 
	from 销售信息
	where 销售日期>=@date1 and 销售日期<=@date2
	select *
	from 进货信息
	where 进货日期>=@date1 and 进货日期<=@date2
end

--添加顾客的存储过程
go
create procedure 添加顾客
    @顾客卡号 nchar(10),
    @顾客姓名 nchar(10),
    @顾客性别 nchar(10),
    @顾客联系方式 nchar(20),
    @顾客年龄 int
    as
    begin
        insert into 顾客信息 values (@顾客卡号,@顾客姓名,@顾客性别,@顾客联系方式,@顾客年龄)
    end;

--更新顾客信息的存储过程
go
create procedure 更新顾客
    @顾客卡号 nchar(10),
    @顾客姓名 nchar(10),
    @顾客性别 nchar(10),
    @顾客联系方式 nchar(20),
    @顾客年龄 int
    as
    begin
        update 顾客信息
        set 顾客姓名 = @顾客姓名,
            顾客性别 = @顾客性别,
            顾客联系方式 = @顾客联系方式,
            顾客年龄 = @顾客年龄
        where 顾客卡号 = @顾客卡号
    end;

--删除顾客的存储过程
go
create procedure 删除顾客
    @顾客卡号 nchar(10)
    as
    begin
        delete 顾客信息
        where 顾客卡号 = @顾客卡号
    end;


--进货过程触发器
go
create trigger 进货过程 on 进货信息
for insert
as
    begin
        update 书店库存
        set 书本数量 = 书本数量 + inserted.进货数量
        from 书店库存 join inserted on 书店库存.图书编号 = inserted.图书编号
    end;

--销售过程触发器
go
create trigger 销售过程 on 销售信息
for insert
as
    begin
        update 书店库存
        set 书本数量 = 书本数量 - inserted.销售数量
        from 书店库存 join inserted on 书店库存.图书编号 = inserted.图书编号
    end;
