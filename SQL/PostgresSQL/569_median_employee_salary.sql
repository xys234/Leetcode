/*


569. Median Employee Salary

The Employee table holds all employees. 
The employee table has three columns: Employee Id, Company Name, and Salary.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|1    | A          | 2341   |
|2    | A          | 341    |
|3    | A          | 15     |
|4    | A          | 15314  |
|5    | A          | 451    |
|6    | A          | 513    |
|7    | B          | 15     |
|8    | B          | 13     |
|9    | B          | 1154   |
|10   | B          | 1345   |
|11   | B          | 1221   |
|12   | B          | 234    |
|13   | C          | 2345   |
|14   | C          | 2645   |
|15   | C          | 2645   |
|16   | C          | 2652   |
|17   | C          | 65     |
+-----+------------+--------+

Write a SQL query to find the median salary of each company. 
Bonus points if you can solve it without using any built-in SQL functions.

+-----+------------+--------+
|Id   | Company    | Salary |
+-----+------------+--------+
|5    | A          | 451    |
|6    | A          | 513    |
|12   | B          | 234    |
|9    | B          | 1154   |
|14   | C          | 2645   |
+-----+------------+--------+



*/


/*


CREATE TABLE Employee
    (Id int, Company varchar(1), Salary int)
;
    
INSERT INTO Employee
    (Id, Company, Salary)
VALUES
    (1, 'A', 2341),
    (2, 'A', 341),
    (3, 'A', 15),
    (4, 'A', 15314),
    (5, 'A', 451),
    (6, 'A', 513),
    (7, 'B', 15),
    (8, 'B', 13),
    (9, 'B', 1154),
    (10, 'B', 1345),
    (11, 'B', 1221),
    (12, 'B', 234),
    (13, 'C', 2345),
    (14, 'C', 2645),
    (15, 'C', 2645),
    (16, 'C', 2652),
    (17, 'C', 65)
;


*/

-- Solution 1: Join. The number of higher salaries - # of lower salaries = 1

WITH Higher AS (
	SELECT E1.Id, E1.Company, E1.Salary, COUNT(E2.Salary) AS Higher
	FROM Employee E1 LEFT JOIN Employee E2 ON (

		E1.Company = E2.Company AND
		E1.Salary < E2.Salary
	)
	GROUP BY E1.Id, E1.Company, E1.Salary
), Lower AS (
	SELECT E1.Id, E1.Company, E1.Salary, COUNT(E2.Salary) AS Lower
	FROM Employee E1 LEFT JOIN Employee E2 ON (

		E1.Company = E2.Company AND
		E1.Salary > E2.Salary
	)
	GROUP BY E1.Id, E1.Company, E1.Salary
), Temp1 AS (
	SELECT H.Company, H.Salary
	FROM Higher H JOIN Lower L ON (
		H.Id = L.Id AND
		H.Company = L.Company AND 
		H.Salary = L.Salary AND
		ABS(Higher - Lower) = 1		
	)
	GROUP BY H.Company, H.Salary
)
SELECT *
FROM Temp1