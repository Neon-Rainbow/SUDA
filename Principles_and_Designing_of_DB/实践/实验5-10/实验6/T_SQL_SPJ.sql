--����SPJ���ݿ��еĲ�ѯ��
use SPJ
--1.ȡ����Ӧ��S1�ṩ���������ɫ��
select distinct color
from pb join spjb on pb.pn = spjb.pn
where spjb.sn = 's1';
--2.ȡ��Ϊ����J1�ṩ��ɫ����Ĺ�Ӧ�̴��ţ�
select distinct sn
from pb join spjb on pb.pn = spjb.pn
where jn = 'J1' and color = '��ɫ';
--3.ȡ��Ϊ���ڳ���Ϊ�Ϻ��Ĺ����ṩ����Ĺ�Ӧ�̴���
select distinct SPJB.sn
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where J.CITY = '�Ϻ�';
--4.ȡ��Ϊ���ڳ���Ϊ�Ϻ��򱱾��Ĺ����ṩ��ɫ����Ĺ�Ӧ�̴��ţ�
select distinct SPJB.SN
from SPJB join PB P on P.PN = SPJB.PN join JB J on J.JN = SPJB.JN join SB S on J.CITY = S.CITY
where P.COLOR = '��ɫ' and J.CITY in ('�Ϻ�','����');
--5.ȡ����Ӧ���빤�����ڳ�����ͬ�Ĺ�Ӧ���ṩ��������ţ�
select distinct SPJB.PN
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where j.CITY = s.CITY;
--6.ȡ���Ϻ��Ĺ�Ӧ���ṩ���Ϻ�����һ���̵�����Ĵ��ţ�
select distinct SPJB.PN
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where j.CITY = '�Ϻ�';
--7.ȡ������������һЩ��CITY��CITY����Ԫ�飬ʹ�õ�1�����еĹ�Ӧ��Ϊ��2�����еĹ����ṩ�����
select distinct s.CITY,j.CITY
from SPJB join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where s.CITY != j.CITY
--8.ȡ��������������Ԫ�飼CITY��PN��CITY����ʹ�õ�1�����еĹ�Ӧ��Ϊ��2�����еĹ����ṩָ���������
select distinct s.CITY,p.PN,j.CITY
from SPJB join PB P on SPJB.PN = P.PN join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where s.CITY = '����1' and j.CITY = '����2' and p.PN = '�����';
--9.�ظ�8�⣬������������CITYֵ��ͬ����Ԫ�顣
select distinct s.CITY,p.PN,j.CITY
from SPJB join PB P on SPJB.PN = P.PN join JB J on J.JN = SPJB.JN join SB S on S.SN = SPJB.SN
where s.CITY = '����1' and j.CITY = '����2' and p.PN = '�����' and s.CITY != j.CITY;
