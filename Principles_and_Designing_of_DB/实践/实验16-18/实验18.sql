USE school
GO
  BACKUP DATABASE school TO DISK='C:\schooldata.bak'

RESTORE FILELISTONLY  FROM DISK='c:\schooldata.bak'
RESTORE HEADERONLY    FROM DISK='c:\schooldata.bak'

USE Master
GO
DROP DATABASE school

RESTORE DATABASE school from DISK='c:\schooldata.bak'

select *
from student

--��
RESTORE DATABASE school from DISK='c:\schoolDiff.bak'WITH file=1 NORECOVERY
RESTORE DATABASE school from DISK='c:\schoolDiff.bak'WITH file=3

Select * from student

ALTER DATABASE school SET RECOVERY FULL;

BACKUP DATABASE school TO DISK = 'C:\schooldata1.bak';

INSERT INTO student VALUES ('7003', '����', '��', 23,null);

BACKUP LOG school TO DISK = 'C:\schoollog.bak';

INSERT INTO student  VALUES ('7004', '����', 'Ů', 22,null);

BACKUP LOG school TO DISK = 'C:\schoollog.bak';

DROP DATABASE school;

RESTORE DATABASE school FROM DISK = 'C:\schooldata1.bak' WITH NORECOVERY;
RESTORE LOG school FROM DISK = 'C:\schoollog.bak' WITH RECOVERY;

--��
