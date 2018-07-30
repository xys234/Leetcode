

/*

615. Average Salary: Departments VS Company

Given two tables as below, write a query to display the comparison result (higher/lower/same) of 
the average salary of employees in a department to the company's average salary.

Table: salary
| id | employee_id | amount | pay_date   |
|----|-------------|--------|------------|
| 1  | 1           | 9000   | 2017-03-31 |
| 2  | 2           | 6000   | 2017-03-31 |
| 3  | 3           | 10000  | 2017-03-31 |
| 4  | 1           | 7000   | 2017-02-28 |
| 5  | 2           | 6000   | 2017-02-28 |
| 6  | 3           | 8000   | 2017-02-28 |

The employee_id column refers to the employee_id in the following table employee.
| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |

So for the sample data above, the result is:
| pay_month | department_id | comparison  |
|-----------|---------------|-------------|
| 2017-03   | 1             | higher      |
| 2017-03   | 2             | lower       |
| 2017-02   | 1             | same        |
| 2017-02   | 2             | same        |


*/



/*
DDL

CREATE TABLE salary
    (id int, employee_id int, amount int, pay_date timestamp)
;
    
INSERT INTO salary
    (id, employee_id, amount, pay_date)
VALUES
    (1, 1, 9000, '2017-03-31 00:00:00'),
    (2, 2, 6000, '2017-03-31 00:00:00'),
    (3, 3, 10000, '2017-03-31 00:00:00'),
    (4, 1, 7000, '2017-02-28 00:00:00'),
    (5, 2, 6000, '2017-02-28 00:00:00'),
    (6, 3, 8000, '2017-02-28 00:00:00')
;


CREATE TABLE employee
    (employee_id int, department_id int)
;
    
INSERT INTO employee
    (employee_id, department_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 2)
;

*/


-- Solution 1: Join with temp tables; Identical to LeetCode article solution
SELECT D.pay_month, department_id, 
( CASE 
	WHEN dept_avg < company_avg THEN 'lower'
	WHEN dept_avg > company_avg THEN 'higher'
	ELSE 'same'
  END
) AS comparison
FROM
(
	SELECT TO_CHAR(pay_date, 'YYYY-MM') AS pay_month, department_id, AVG(amount) AS dept_avg
	FROM salary AS S JOIN employee AS E ON (

		S.employee_id = E.employee_id
	)
	GROUP BY TO_CHAR(pay_date, 'YYYY-MM'), department_id
) AS D INNER JOIN
(
	SELECT TO_CHAR(pay_date, 'YYYY-MM') AS pay_month, AVG(amount) AS company_avg
	FROM salary AS S JOIN employee AS E ON (

		S.employee_id = E.employee_id
	)
	GROUP BY TO_CHAR(pay_date, 'YYYY-MM')
) AS C ON (

	D.pay_month = C.pay_month

)
ORDER BY D.pay_month DESC, department_id ASC




