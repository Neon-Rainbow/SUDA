use school
create index ix_student_sname on student(sname);
create index ix_student_sdept on student(Sdept);
create index ix_sc_cno on sc(cno);
create unique index ix_course_cname on course(cname);

exec sp_helpindex student;
exec sp_helpindex sc;
exec sp_helpindex course;

drop index ix_course_cname on Course;

drop index ix_student_sname on Student;
create unique index ix_student_sname on student(sname);