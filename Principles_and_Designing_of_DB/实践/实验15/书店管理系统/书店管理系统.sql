--�������ݿ�
create database ������ϵͳ

use ������ϵͳ

--������
create table �����(
	ͼ���� nchar(10) primary key,
	�鱾��� nchar(10) not null,
	�鱾���� int not null,
)

create table �鱾��Ϣ(
	ͼ���� nchar(10) foreign key references �����(ͼ����),
	�鱾��� nchar(10) not null,
	�鱾���� nchar(10) not null,
	�鱾ҳ�� int not null,
	�鱾������ nchar(10) not null,
	�鱾�۸� float not null,
)

create table �˿���Ϣ(
	�˿Ϳ��� nchar(10) not null primary key,
	�˿����� nchar(10) not null,
	�˿��Ա� nchar(10) not null check(�˿��Ա� in('��','Ů')),
	�˿���ϵ��ʽ nchar(20) not null,
	�˿����� int not null,
)

create table ������Ϣ(
	���۵��� nchar(10) not null primary key,
	ͼ���� nchar(10) not null foreign key references �����(ͼ����),
	�˿Ϳ��� nchar(10) not null foreign key references �˿���Ϣ(�˿Ϳ���),
	�������� int not null,
	�������� date default(getdate()),
	���۽�� float default(0),
)

create table ��Ӧ����Ϣ(
	�����̺�   nchar(10) not null primary key,
	���������� nchar(10) not null,
	�����̵绰 nchar(10) not null,
	�����̵�ַ nchar(10) not null,
)

create table ������Ϣ(
	�������� nchar(10) not null primary key,
	ͼ���� nchar(10) not null foreign key references �����(ͼ����),
	�鱾��� nchar(10) not null,
	��Ӧ�̺� nchar(10) not null foreign key references ��Ӧ����Ϣ(�����̺�),
	�������� int not null,
	�������� date default(getdate())
)

--�洢����
--���仯�Ĵ洢����
go
create procedure ���仯
	@date1 date,
	@date2 date
as
begin
	select * 
	from ������Ϣ
	where ��������>=@date1 and ��������<=@date2
	select *
	from ������Ϣ
	where ��������>=@date1 and ��������<=@date2
end

--��ӹ˿͵Ĵ洢����
go
create procedure ��ӹ˿�
    @�˿Ϳ��� nchar(10),
    @�˿����� nchar(10),
    @�˿��Ա� nchar(10),
    @�˿���ϵ��ʽ nchar(20),
    @�˿����� int
    as
    begin
        insert into �˿���Ϣ values (@�˿Ϳ���,@�˿�����,@�˿��Ա�,@�˿���ϵ��ʽ,@�˿�����)
    end;

--���¹˿���Ϣ�Ĵ洢����
go
create procedure ���¹˿�
    @�˿Ϳ��� nchar(10),
    @�˿����� nchar(10),
    @�˿��Ա� nchar(10),
    @�˿���ϵ��ʽ nchar(20),
    @�˿����� int
    as
    begin
        update �˿���Ϣ
        set �˿����� = @�˿�����,
            �˿��Ա� = @�˿��Ա�,
            �˿���ϵ��ʽ = @�˿���ϵ��ʽ,
            �˿����� = @�˿�����
        where �˿Ϳ��� = @�˿Ϳ���
    end;

--ɾ���˿͵Ĵ洢����
go
create procedure ɾ���˿�
    @�˿Ϳ��� nchar(10)
    as
    begin
        delete �˿���Ϣ
        where �˿Ϳ��� = @�˿Ϳ���
    end;


--�������̴�����
go
create trigger �������� on ������Ϣ
for insert
as
    begin
        update �����
        set �鱾���� = �鱾���� + inserted.��������
        from ����� join inserted on �����.ͼ���� = inserted.ͼ����
    end;

--���۹��̴�����
go
create trigger ���۹��� on ������Ϣ
for insert
as
    begin
        update �����
        set �鱾���� = �鱾���� - inserted.��������
        from ����� join inserted on �����.ͼ���� = inserted.ͼ����
    end;
