> 2127405048 方浩楠

# 2.1

> Consider the employee database of Figure 2.17. What are the appropriate primary-keys?

主键用下划线标记

employee(<u>person_name</u>, street, city)
works(<u>person_name</u>, company_name, salary)
company(<u>company_name</u>, city)

# 2.4

> In the instance of *instructor* shown in Figure 2.1, no two instructors have the same name. From this, can we conclude that *name* can be used as a superkey (or primary key) of *instructor*?

不能,除非学校规定不能有两个老师取一样的名字,不然就不能使用name作为主键

# 2.6

> Consider the *advisor* relation shown in the schema diagram in Figure 2.9, with *s_id* as the primary key of *advisor*. Suppose a student can have more than one advisor. Then, would *s_id* still be a primary key of the *advisor* relation? If not, what should the primary key of *advisor* be?

不是,因为一个学生可以有多个顾问
