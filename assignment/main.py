
#31.
# INSERT INTO employees (id, name, department, salary)
# VALUES (1, 'Alice', 'HR', 50000);

#32.
# INSERT INTO employees (id, name, department, salary)
# VALUES 
# (2, 'Bob', 'IT', 60000),
# (3, 'Charlie', 'Finance', 55000),
# (4, 'Diana', 'Marketing', 52000);

#33.
# UPDATE employees
# SET salary = 58000
# WHERE department = 'Finance';

#34.
# DELETE FROM employees
# WHERE department = 'Marketing';

#35.
#SELECT * FROM employees;

#36.
#SELECT name, salary FROM employees;

#37.
#SELECT DISTINCT department FROM employees;

#38.
# SELECT * FROM employees
# LIMIT 5;

#39.
# UPDATE employees
# SET name = 'Robert', salary = 62000
# WHERE id = 2;

#40.
#DELETE FROM employees;

#41.
# CREATE TABLE employees (
#     id INT PRIMARY KEY,
#     name VARCHAR(100)
# );

#42.
# -- FOREIGN KEY example
# CREATE TABLE departments (
#     dept_id INT PRIMARY KEY,
#     dept_name VARCHAR(50)
# );

# CREATE TABLE employees (
#     emp_id INT PRIMARY KEY,
#     name VARCHAR(100),
#     dept_id INT,
#     FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
# );

# 43.
# CREATE TABLE users (
#     id INT,
#     email VARCHAR(100) UNIQUE
# );

# 44.
# CREATE TABLE students (
#     id INT NOT NULL,
#     name VARCHAR(50) NOT NULL
# );

# 45.
# CREATE TABLE orders (
#     id INT,
#     status VARCHAR(20) DEFAULT 'pending'
# );

# 46.
# CREATE TABLE products (
#     id INT,
#     price DECIMAL(10,2),
#     CHECK (price >= 0)
# );

# 47.
# no table cant have multiple primary keys

# 48.
# ALTER TABLE table_name
# DROP CONSTRAINT constraint_name;
# ----------------------------------------
# ALTER TABLE table_name DROP PRIMARY KEY;
# ALTER TABLE table_name DROP FOREIGN KEY fk_name;

# 49.
# error

#50.
# CREATE TABLE enrollment (
#     student_id INT,
#     course_id INT,
#     PRIMARY KEY (student_id, course_id)
# );

#51.
# INNER JOIN: Returns only the matching rows from both tables.

# OUTER JOIN: Returns matching rows plus unmatched rows from one or both tables:

# LEFT JOIN = all rows from left table + matched rows from right

# RIGHT JOIN = all rows from right table + matched rows from left

# FULL OUTER JOIN = all rows from both tables (MySQL doesn't support it directly)


#52.
# SELECT employees.name, departments.dept_name
# FROM employees
# INNER JOIN departments ON employees.dept_id = departments.dept_id;

#53.
# SELECT employees.name, departments.dept_name
# FROM employees
# LEFT JOIN departments ON employees.dept_id = departments.dept_id;

#54.
# SELECT employees.name, departments.dept_name
# FROM employees
# RIGHT JOIN departments ON employees.dept_id = departments.dept_id;

#55.
# SELECT e.name, d.dept_name
# FROM employees e
# LEFT JOIN departments d ON e.dept_id = d.dept_id

# UNION

# SELECT e.name, d.dept_name
# FROM employees e
# RIGHT JOIN departments d ON e.dept_id = d.dept_id;

# 56.
# SELECT color.name, size.label
# FROM color
# CROSS JOIN size;

#57.
# SELECT a.name AS employee, b.name AS manager
# FROM employees a
# JOIN employees b ON a.manager_id = b.emp_id;

# 58.
# SELECT o.order_id, c.name, p.product_name
# FROM orders o
# JOIN customers c ON o.customer_id = c.customer_id
# JOIN products p ON o.product_id = p.product_id;

# 59.
# ON is used to define join condition between tables.

# WHERE is used to filter rows after the join has happened.

# -- Join condition using ON
# SELECT * FROM A
# JOIN B ON A.id = B.a_id
# WHERE B.status = 'active';  -- Filtering result

# 60.
# SELECT * 
# FROM employees
# NATURAL JOIN departments;
