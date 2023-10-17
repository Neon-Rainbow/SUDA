> 2127405048 方浩楠

# 2.2

> Consider the foreign-key constraint from the *dept_name* attribute of *instructor* to the *department* relation. Give examples of inserts and deletes to these relations that can cause a violation of the foreign-key constraint.

1.

插入一个元组,其中元组的dept_name不在department中,这样会违反外键约束

2.

删除department中的(Biology,Watson,90000),这样会导致course中的老师违反外键约束

# 2.9

> List two reasons why null values might be introduced into a database.

1.属性的值为空

2.属性的值不存在

# 3.13

>Write SQL DDL corresponding to the schema in Figure 3.17. Make any reasonable assumptions about data types, and be sure to declare primary and foreign keys.

```sql
CREATE TABLE person (
    driver_id VARCHAR(15) PRIMARY KEY,
    name VARCHAR(30) NOT NULL, 
    address VARCHAR(40)
);

CREATE TABLE car (
    license_plate VARCHAR(8) PRIMARY KEY, 
    model VARCHAR(7), 
    year NUMERIC(4,0) CHECK (year > 1701 AND year < 2100), 
);

CREATE TABLE accident ( 
    report_number VARCHAR(10) PRIMARY KEY, 
    year NUMERIC(4,0) CHECK (year > 1701 AND year < 2100),
    location VARCHAR(30)
);

CREATE TABLE owns (
    driver_id VARCHAR(15),
    license_plate VARCHAR(8),
    PRIMARY KEY (driver_id, license_plate), 
    FOREIGN KEY (driver_id) REFERENCES person(driver_id) 
    FOREIGN KEY (license_plate) REFERENCES car(license_plate)
);

CREATE TABLE participated ( 
    report_number VARCHAR(10), 
    license_plate VARCHAR(8), 
    driver_id VARCHAR(15),
    damage_amount NUMERIC(10,2),
    PRIMARY KEY(report_number, license_plate),
    FOREIGN KEY (report_number) REFERENCES accident(report_number), 
    FOREIGN KEY (license_plate) REFERENCES car(license_plate)
);
```

# 4.7

> Consider the employee database of Figure 4.12. Give an SQL DDL definition of this database. Identify referential-integrity constraints that should hold, and include them in the DDL definition.

```SQL
CREATE TABLE employee ( 
    id INTEGER PRIMARY KEY ,
    person_name VARCHAR(50),
    street VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE company ( 
    company_name VARCHAR(50)  PRIMARY KEY,
    city VARCHAR(50),
);

CREATE TABLE works (
    id INTEGER PRIMARY KEY,
    company_name VARCHAR(50),
    salary numeric(10,2),
    FOREIGN KEY (id) REFERENCES employee(id),
    FOREIGN KEY (company_name) REFERENCES company(company_name)
);

CREATE TABLE manages ( 
    id INTEGER PRIMARY KEY,
    manager_id INTEGER, 
    FOREIGN KEY (id) REFERENCES employee (id), 
    FOREIGN KEY (manager_id) REFERENCES employee (id)
)
```

# 4.9

> SQL allows a foreign-key dependency to refer to the same relation, as in the following
> example: 
>
> ```sql
> CREATE TABLE manager ( 
>  employee_id char(20),
>  manager_id char(20), 
>  PRIMARY KEY employee_id,
>  FOREIGN KEY (manager_id) REFERENCES manager (employee_id)
>      ON DELETE CASCADE
> ); 
> ```
> Here, _employee_id_ is a key to the table _manager_, meaning that each employee has at 
> at most one manager. The foreign-key clause requires that every manager also be an employee. 
> Explain exactly what happens when a tuple in the relation _manager_ is deleted. 

该manager的所有employee的信息都会被删除