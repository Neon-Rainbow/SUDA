use AdventureWorks2019
--1.在Product 表中查出所有产品信息（三列：Name, ProductNumber, ListPrice） ，按产品名升序排列
select Name,ProductNumber,ListPrice
from Production.Product
order by Name asc;

--2.在Product表中查出标价大于$1000的产品，求出这些产品的均价并按类型号分组
select ProductModelID,avg(ListPrice) as '均价'
from Production.product
where ListPrice>1000
group by ProductModelID;

--3.在Product表中查出每种产品类型均价等于该类产品最高标价的产品类型号
select ProductModelID
from Production.Product
group by ProductModelID
having avg(ListPrice) = max(ListPrice);

--4.在SalesOrderDetail表中查出每个销售订单的销售总额。两列：订单号、销售总额
select ProductID as '订单号',sum(UnitPrice) as '销售总额'
from Sales.SalesOrderDetail
group by ProductID;

--5.在SalesOrderDetail表中查出每种产品销售平均价格以及该产品迄今为止的总销售额。三列：ID、均价、总额
select ProductID as ID,avg(UnitPrice) as '均价', sum(UnitPrice) as '总额'
from Sales.SalesOrderDetail
group by ProductID;

--6在SalesOrderDetail表中查出总销量大于5的产品 ID，并排序。 必须使用 HAVING
select ProductID,sum(OrderQty)
from Sales.SalesOrderDetail
group by ProductID
having sum(OrderQty)>5
order by sum(OrderQty) desc;

--7.在SalesOrderDetail表中查出单价小于25，且平均订单量大于5的产品 ID
select ProductID
from Sales.SalesOrderDetail
group by ProductID
having avg(OrderQty)>5 and max(UnitPrice)<25

--8.在SalesOrderDetail表中查出总销售额大于$10000 且平均单笔销量小于3的产品。三列：ID、均价、总销售额
select ProductID as ID,avg(UnitPrice) as '均价',sum(LineTotal) as '总销售额'
from Sales.SalesOrderDetail
group by ProductID
having sum(LineTotal) > 10000 and avg(OrderQty)<3;

--9.在SalesOrderDetail表中查出单笔销售产品数量大于 10 的订单销售的产品 ID 和均价。分组。
select ProductID as ID,avg(UnitPrice) as '均价'
from Sales.SalesOrderDetail
where OrderQty>10
group by ProductID;

--10.在SalesOrderDetail表中查出完成了相同单笔销售额的订单的平均销售产品数量和这个销售总额。
select avg(OrderQty),sum(LineTotal)
from Sales.SalesOrderDetail
group by LineTotal
having count(*)>1;
--11.查出每种产品的销售总额和折扣总额。涉及表：Product、SalesOrderDetail，按产品名升序排列。共三列，必须使用 join。
select p.Name as '产品名字',sum(LineTotal) as '销售总额',sum(s.UnitPriceDiscount * s.OrderQty*UnitPrice) as '折扣总额'
from Production.Product as p join Sales.SalesOrderDetail as s on p.ProductID = s.ProductID
group by p.ProductID,p.Name
order by p.Name asc;
--12查出销售订单中每种产品的收入金额（扣除折扣后）。涉及表 ： Product、 SalesOrderDetail，按产品名降序排列。共三列。必须使用 join。
select p.Name,sum((1-UnitPriceDiscount)*UnitPrice*s.OrderQty) as '收入金额'
from Production.Product as p join Sales.SalesOrderDetail as s on p.ProductID = s.ProductID
group by p.ProductID,p.Name
order by p.Name desc;

--13.查出产品型号为“Long-Sleeve Logo Jersey*” （*为任意字符）的每种产品名。涉及表：Product、ProductModel。一列，使用 EXISTS 和 IN 两种方法完成。 
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
--14.在SalesOrderDetail表中统计订单中至少包含9项产品的产品ID及其销售总额。 
select ProductID,sum(LineTotal)
from Sales.SalesOrderDetail as SOD
group by ProductID
having count(*) >= 9;