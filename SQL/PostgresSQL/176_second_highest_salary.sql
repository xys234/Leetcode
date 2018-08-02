


/*

176. Second Highest Salary

Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+


*/



-- Solution 1: Join

SELECT COALESCE(
(
    SELECT E1.Salary 
    FROM Employee E1 JOIN Employee E2 ON (

        E1.Salary < E2.Salary

    )
    GROUP BY E1.Salary
    HAVING COUNT(DISTINCT E2.Salary) = 1
)
, NULL) AS SecondHighestSalary



-- Solution 2: LIMIT and OFFSET

SELECT COALESCE(
(
    SELECT DISTINCT Salary
	FROM Employee
	ORDER BY Salary DESC
	LIMIT 1 OFFSET 1
)
, NULL) AS SecondHighestSalary




