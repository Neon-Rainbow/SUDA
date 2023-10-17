use AdventureWorks2019
--1.��Product ���в�����в�Ʒ��Ϣ�����У�Name, ProductNumber, ListPrice�� ������Ʒ����������
select Name,ProductNumber,ListPrice
from Production.Product
order by Name asc;

--2.��Product���в����۴���$1000�Ĳ�Ʒ�������Щ��Ʒ�ľ��۲������ͺŷ���
select ProductModelID,avg(ListPrice) as '����'
from Production.product
where ListPrice>1000
group by ProductModelID;

--3.��Product���в��ÿ�ֲ�Ʒ���;��۵��ڸ����Ʒ��߱�۵Ĳ�Ʒ���ͺ�
select ProductModelID
from Production.Product
group by ProductModelID
having avg(ListPrice) = max(ListPrice);

--4.��SalesOrderDetail���в��ÿ�����۶����������ܶ���У������š������ܶ�
select ProductID as '������',sum(UnitPrice) as '�����ܶ�'
from Sales.SalesOrderDetail
group by ProductID;

--5.��SalesOrderDetail���в��ÿ�ֲ�Ʒ����ƽ���۸��Լ��ò�Ʒ����Ϊֹ�������۶���У�ID�����ۡ��ܶ�
select ProductID as ID,avg(UnitPrice) as '����', sum(UnitPrice) as '�ܶ�'
from Sales.SalesOrderDetail
group by ProductID;

--6��SalesOrderDetail���в������������5�Ĳ�Ʒ ID�������� ����ʹ�� HAVING
select ProductID,sum(OrderQty)
from Sales.SalesOrderDetail
group by ProductID
having sum(OrderQty)>5
order by sum(OrderQty) desc;

--7.��SalesOrderDetail���в������С��25����ƽ������������5�Ĳ�Ʒ ID
select ProductID
from Sales.SalesOrderDetail
group by ProductID
having avg(OrderQty)>5 and max(UnitPrice)<25

--8.��SalesOrderDetail���в�������۶����$10000 ��ƽ����������С��3�Ĳ�Ʒ�����У�ID�����ۡ������۶�
select ProductID as ID,avg(UnitPrice) as '����',sum(LineTotal) as '�����۶�'
from Sales.SalesOrderDetail
group by ProductID
having sum(LineTotal) > 10000 and avg(OrderQty)<3;

--9.��SalesOrderDetail���в���������۲�Ʒ�������� 10 �Ķ������۵Ĳ�Ʒ ID �;��ۡ����顣
select ProductID as ID,avg(UnitPrice) as '����'
from Sales.SalesOrderDetail
where OrderQty>10
group by ProductID;

--10.��SalesOrderDetail���в���������ͬ�������۶�Ķ�����ƽ�����۲�Ʒ��������������ܶ
select avg(OrderQty),sum(LineTotal)
from Sales.SalesOrderDetail
group by LineTotal
having count(*)>1;
--11.���ÿ�ֲ�Ʒ�������ܶ���ۿ��ܶ�漰��Product��SalesOrderDetail������Ʒ���������С������У�����ʹ�� join��
select p.Name as '��Ʒ����',sum(LineTotal) as '�����ܶ�',sum(s.UnitPriceDiscount * s.OrderQty*UnitPrice) as '�ۿ��ܶ�'
from Production.Product as p join Sales.SalesOrderDetail as s on p.ProductID = s.ProductID
group by p.ProductID,p.Name
order by p.Name asc;
--12������۶�����ÿ�ֲ�Ʒ��������۳��ۿۺ󣩡��漰�� �� Product�� SalesOrderDetail������Ʒ���������С������С�����ʹ�� join��
select p.Name,sum((1-UnitPriceDiscount)*UnitPrice*s.OrderQty) as '������'
from Production.Product as p join Sales.SalesOrderDetail as s on p.ProductID = s.ProductID
group by p.ProductID,p.Name
order by p.Name desc;

--13.�����Ʒ�ͺ�Ϊ��Long-Sleeve Logo Jersey*�� ��*Ϊ�����ַ�����ÿ�ֲ�Ʒ�����漰��Product��ProductModel��һ�У�ʹ�� EXISTS �� IN ���ַ�����ɡ� 
select p.Name
from Production.Product as p
where p.ProductModelID in(
	select pm.ProductModelID
	from Production.ProductModel as pm
	where Name like 'Long-Sleeve Logo Jersey%'
);
select distinct Name
from Production.Product as p
where exists(
	select *
	from Production.ProductModel as pm
	where p.ProductModelID = pm.ProductModelID and pm.Name like 'Long-Sleeve Logo Jersey%'
);
--14.��SalesOrderDetail����ͳ�ƶ��������ٰ���9���Ʒ�Ĳ�ƷID���������ܶ 
select ProductID,sum(LineTotal)
from Sales.SalesOrderDetail as SOD
group by ProductID
having count(*) >= 9;