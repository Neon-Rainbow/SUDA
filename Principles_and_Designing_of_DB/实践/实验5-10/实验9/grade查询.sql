--������µ�SQL��ѯ������Ӧ��SQL���д��ÿ����Ŀ���·�
use grade
--1����ѯѧ����ȫ����Ϣ��
select *
from s;

--2����ѯѡ���˿γ̵�ѧ���š�
select distinct sno
from sc;

--3����ѯѡ�޿γ̺�Ϊ��C1����ѧ����ѧ�źͳɼ���
select sno,score
from sc
where cno = 'C1';

--4����ѯ�ɼ�����85�ֵ�ѧ����ѧ�š��γ̺źͳɼ���
select sno,cno,score
from sc
where score>85;

--5����ѯѡ��C1��C2�ҷ������ڵ���85��ѧ���ĵ�ѧ�š��γ̺źͳɼ���
select sno,cno,score
from sc
where cno in('C1','C2') and score>85;

--6����ѯ������1000��1500֮��Ľ�ʦ�Ľ�ʦ�š�������ְ�ơ�
select tno,tn,prof
from t
where sa between 1000 and 1500;

--7����ѯû��ѡ��C1��Ҳû��ѡ��C2��ѧ����ѧ�š��γ̺źͳɼ���
select sno, cno, score 
from SC 
where sno not in (
	select sno 
	from SC 
	where cno in ('c1','c2'));

--8����ѯ�������ŵĽ�ʦ�Ľ�ʦ�ź�������
select tno,tn
from t
where tn like '��%';

--9����ѯ�����еڶ��������ǡ������Ľ�ʦ�ź�������
select tno,tn
from t
where tn like '_��%';

--10����ѯû�п��Գɼ���ѧ����ѧ�ź���Ӧ�Ŀγ̺š�
select sno,cno
from sc
where score is null;

--11����ѯѡ��C1 ��ѧ��ѧ�źͳɼ��������ɼ��������С�
select sno,score
from sc
where cno = 'c1'
order by score desc;

--12����ѯѡ��C1��C2��ѧ�š��γ̺źͳɼ�����ѯ�����ѧ���������У�ѧ����ͬ�ٰ��ɼ��������С�
select sno,cno,score
from sc
where cno in ('c1','c2')
order by sno,score desc;

--13. ��ѧ��ΪS1ѧ�����ֺܷ�ƽ���֡�
select max(score) as max_score,avg(score) as avg_score
from sc
where sno = 's1'��

--14����ѡ��C1�ſγ̵���߷֡���ͷּ�֮�����ķ���
select max(score),min(score),max(score)-min(score)
from sc
where cno = 'C1';

--15��������ϵѧ��������
select count(*)
from s join dep on s.DEPtid = dep.DEPtid
where depname = '�����ϵ';

--16����ѯ��λ��ʦ�Ľ�ʦ�ż����οε�������
select tno,count(distinct cno)
from tc 
group by tno;

--17����ѯѡ���������Ͽγ̵�ѧ��ѧ�ź�ѡ������
select sno,count(distinct cno)
from sc
group by sno
having count(distinct sno)>2;

--18����ѡ�������������Ҹ��ſγ̾������ѧ����ѧ�ż����ܳɼ�����ѯ������ܳɼ������г���
select sno,sum(score)
from sc
group by sno
having count(distinct cno)>3 and min(score)>=60
order by sum(score);

--19����ѯ��������ʦְ����ͬ�Ľ�ʦ�š�������
select t1.tno,t1.tn
from t as t1,t as t2
where t1.prof = t2.prof and t2.tn = '����' and t1.tno != t2.tno

--20����ѯ���ڿγ̺�ΪC1�Ľ�ʦ������
select tn
from t join tc on t.tno=tc.tno
where cno = 'C1';

--21����ѯ���ڿγ̺�ΪC1�Ľ�ʦ������ϵ���Ϳγ�����
select tn,deptid,cname
from t,tc,course
where t.tno = tc.tno and course.cno = tc.cno and tc.cno = 'c1'

--22����ѯ�����ϵ��ѧ��ѡ�޿γ̵Ŀγ�����ѧ�š��ɼ�
select course.cname,s.sno,sc.score
from course,s,sc,dep
where course.cno = sc.cno and sc.sno = s.sno and dep.DEPtid = s.DEPtid and dep.DEPname = '�����ϵ'

--23����ѯ��������ѡ�޵Ŀγ����� 
select cname
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and s.sname = '����';

--24����ѯ��������ѡ�޵Ŀγ����ͳɼ���
select cname,score
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and s.sname = '����';

--25����ѯ'����'���ܷ֡�ƽ����
select sum(score) as '�ܷ�', avg(score) as 'ƽ����'
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and s.sname = '����';

--26����ʾѧ����������ѧ����ƽ����
select sname,avg(score) as 'ƽ����'
from s join sc on s.sno = sc.sno
group by s.sname;

--27����ʾѧ��ѧ�š�ѧ����������ѧ����ƽ����
select s.sno,sname,avg(score) as 'ƽ����'
from s join sc on s.sno = sc.sno
group by s.sno,sname;

--28����ѯÿһ�ſεļ�����޿Σ������޿ε����޿Σ�
select c1.cname as '�γ���',c2.cname '���޿γ���'
from course as c1,course as c2
where c1.pcno = c2.cno;

--29����ѯѡ��c1�ſγ��ҳɼ���70�����ϵ�����ѧ������ϸ��Ϣ
select s.sno,sname,age,deptid
from s join sc on s.sno = sc.sno
where sc.cno = 'c1' and score > 70;

--30.  ��ѯ�롰��������ͬһ��ϵѧϰ��ѧ������
select s1.sname
from s as s1,s as s2
where s2.Sname = '����' and s1.sno != s2.Sno and s1.DEPtid = s2.DEPtid;

--31.��ѯѡ���˿γ���Ϊ�������ԭ����ѧ��ѧ�ź�����
select s.sno,sname 
from s,sc,course
where s.sno = sc.sno and sc.cno = course.cno and cname = '�����ԭ��';

--32.��ѯ����ϵ�бȼ����ϵ����ѧ�����䶼С��ѧ�����������䡣
with min_age_cmop(min_age) as(
	select min(age)
	from s,dep
	where s.DEPtid = dep.DEPtid and dep.DEPname = '�����ϵ'
)
select sname,age
from s,dep,min_age_cmop
where s.DEPtid = dep.DEPtid and dep.DEPname != '�����ϵ' and s.age < min_age; 

--33.��ѯû��ѡ�ε�ѧ��������
select sname
from s left outer join sc on s.sno = sc.Sno
where cno IS NULL;

--34.�ҳ��ɼ���������ѡ�޿γ�ƽ���ɼ���ѧ�źͳɼ���
with avg_score(value) as(
	select avg(score)
	from sc
)
select s.sno,sc.score
from s,sc,avg_score
where s.sno = sc.sno and sc.score > avg_score.value;

--35����ѯ����ϵ�бȼ����ϵ���н�ʦ���ʶ��ߵĽ�ʦ�������͹��ʡ�
with max_salary(salary) as(
	select max(sa)
	from t join dep on t.DEPtid = dep.DEPtid
	where depname = '�����ϵ'
)
select tn,sa
from t,dep,max_salary
where t.DEPtid = DEP.DEPtid and DEP.DEPname = '�����ϵ' and t.SA > max_salary.salary

--36.��������ѡ������ΰ��ʦ���ڿγ���һ�ſγ̵�ѧ��������
with liuwei_class(cno) as(
	select cno
	from t join tc on t.tno = tc.tno
	where t.tn = '��ΰ'
) 
select sname
from s,sc,liuwei_class
where sc.sno = s.sno and sc.cno = liuwei_class.cno;

--37.�������ͬѧ��ѧ�Ŀγ̵Ŀγ̺�
select distinct sc.cno
from sc
except
select distinct sc.cno
from sc join s on sc.sno = s.sno
where s.sname = '���'

--20.��û��ѡ�ޡ����ݿ�ԭ���γ̵�ѧ����������
select sname 
from s 
where sno not in (
	select sno 
	from sc,course 
	where sc.cno=course.cno and course.cname='���ݿ�ԭ��'
)

--38.��ѯ�����ϵ��ѧ�������䲻����19���ѧ���Ľ���
select s.sno
from s join dep on s.DEPtid = dep.DEPtid
where dep.DEPname = '�����ϵ'
intersect
select sno
from s
where age<=19

--39.��ѯѡ�޿γ�c1��ѧ��������ѡ�޿γ�c2��ѧ�����ϵĽ���
select sno 
from sc 
where cno='c1' 
intersect 
select sno 
from sc 
where cno='c2'

--40.��ѯ�����ϵ��ѧ�������䲻����19���ѧ���Ĳ��
select s.sno
from s join dep on s.DEPtid = dep.DEPtid
where dep.DEPname = '�����ϵ'
except
select sno
from s
where age<=19