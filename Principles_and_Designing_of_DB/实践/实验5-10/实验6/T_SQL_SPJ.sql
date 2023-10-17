--二．SPJ数据库中的查询：
use SPJ
--1.取出供应商S1提供的零件的颜色；
select distinct color
from pb join spjb on pb.pn = spjb.pn
where spjb.sn = 's1';
--2.取出为工程J1提供红色零件的供应商代号；
select distinct sn
from pb join spjb on pb.pn = spjb.pn
where jn = 'J1' and color = '红色';
--3.取出为所在城市为上海的工程提供零件的供应商代号
select distinct SPJB.sn
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where J.CITY = '上海';
--4.取出为所在城市为上海或北京的工程提供红色零件的供应商代号；
select distinct SPJB.SN
from SPJB join PB P on P.PN = SPJB.PN join JB J on J.JN = SPJB.JN join SB S on J.CITY = S.CITY
where P.COLOR = '红色' and J.CITY in ('上海','北京');
--5.取出供应商与工程所在城市相同的供应商提供的零件代号；
select distinct SPJB.PN
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where j.CITY = s.CITY;
--6.取出上海的供应商提供给上海的任一工程的零件的代号；
select distinct SPJB.PN
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where j.CITY = '上海';
--7.取出所有这样的一些＜CITY，CITY＞二元组，使得第1个城市的供应商为第2个城市的工程提供零件；
select distinct s.CITY,j.CITY
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where s.CITY != j.CITY
--8.取出所有这样的三元组＜CITY，PN，CITY＞，使得第1个城市的供应商为第2个城市的工程提供指定的零件；
select distinct s.CITY,p.PN,j.CITY
from SPJB join PB P on SPJB.PN = P.PN join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where s.CITY = '城市1' and j.CITY = '城市2' and p.PN = '零件号';
--9.重复8题，但不检索两个CITY值相同的三元组。
select distinct s.CITY,p.PN,j.CITY
from SPJB join PB P on SPJB.PN = P.PN join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where s.CITY = '城市1' and j.CITY = '城市2' and p.PN = '零件号' and s.CITY != j.CITY;
