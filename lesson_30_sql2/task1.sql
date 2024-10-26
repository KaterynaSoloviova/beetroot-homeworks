-- Task 1
-- Joins
-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)
-- As a solution to HW, create a file named: task1.sql with all SQL queries:

-- write a query in SQL to display the first name, last name, department number, and department name for each employee

SELECT first_name, last_name, employees.department_id, department_name
FROM employees
         JOIN department ON employees.department_id = department.department_id;

-- write a query in SQL to display the first and last name, department, city, and state province for each employee

SELECT first_name, last_name, city, state_province
FROM employees AS e
         JOIN department as d ON e.department_id = d.department_id
         JOIN locations as l ON l.location_id = d.location_id;

-- write a query in SQL to display the first name, last name, department number, and department name, for all employees
-- for departments 80 or 40

SELECT first_name, last_name, employees.department_id, department_name
FROM employees
         JOIN department ON employees.department_id = department.department_id
WHERE employees.department_id = 80
   OR employees.department_id = 40;

-- write a query in SQL to display all departments including those where does not have any employee

SELECT d.department_id, d.department_name, e.first_name, e.last_name
FROM department d
         LEFT JOIN employees e ON d.department_id = e.department_id;

-- write a query in SQL to display the first name of all employees including the first name of their manager

SELECT e.first_name AS "Employeer First Name", m.first_name AS "Manager First Name"
FROM employees e
         JOIN employees m ON e.manager_id = m.employee_id;

-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference
-- between the maximum salary for the job and the salary of the employee

SELECT j.job_title                            AS "Job Title",
       CONCAT(e.first_name, ' ', e.last_name) AS "Full Name",
       j.max_salary - e.salary                AS "Salary Difference"
FROM employees e
         JOIN jobs j ON e.job_id = j.job_id;

-- write a query in SQL to display the job title and the average salary of employees

SELECT j.job_title AS "Job Title", AVG(e.salary) AS "Average Salary"
FROM employees e
         JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;

-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any
-- department located in London

SELECT CONCAT(e.first_name, ' ', e.last_name) AS "Full Name", l.city, e.salary
FROM employees AS e
         JOIN department as d ON e.department_id = d.department_id
         JOIN locations as l ON l.location_id = d.location_id
WHERE l.city = 'London';

-- write a query in SQL to display the department name and the number of employees in each department

SELECT d.department_name AS "Department Name", COUNT(1) AS "Employees Number"
FROM department d
         JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;