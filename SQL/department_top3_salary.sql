-- The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.
-- 
-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- | 5  | Janet | 69000  | 1            |
-- | 6  | Randy | 85000  | 1            |
-- +----+-------+--------+--------------+
-- The Department table holds all departments of the company.
-- 
-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- Write a SQL query to find employees who earn the top three salaries in each of the department. For the above tables, your SQL query should return the following rows.
-- 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | IT         | Randy    | 85000  |
-- | IT         | Joe      | 70000  |
-- | Sales      | Henry    | 80000  |
-- | Sales      | Sam      | 60000  |
-- +------------+----------+--------+


-----------  MySQL Attempt --------------  
SELECT Department, Employee, Salary FROM
(
	SELECT D.Name AS Department, E.Name AS Employee, Salary
	FROM Employee AS E JOIN Department AS D ON
	(
		E.DepartmentId = D.Id

	)

) AS T
WHERE Employee IN
(
	SELECT a.Employee 
	FROM (
	
		SELECT D.Name AS Department, E.Name AS Employee, Salary
		FROM Employee AS E JOIN Department AS D ON
		(
			E.DepartmentId = D.Id

		)
	) 
	AS a 
	LEFT JOIN 
	(
		SELECT D.Name AS Department, E.Name AS Employee, Salary
		FROM Employee AS E JOIN Department AS D ON
		(
			E.DepartmentId = D.Id

		)
	) 
	AS b 
		ON a.Department = b.Department AND a.Salary < b.Salary
	GROUP BY a.Employee
	HAVING COUNT(DISTINCT b.Salary) <= 2
	ORDER BY a.Department, a.Salary DESC
)
ORDER BY Department, Salary DESC


-----------  MySQL ANSWER --------------
SELECT
    d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;


-----------  SQL Server Attempt -------------- 

SELECT Department, Employee, Salary
FROM 
(
	SELECT Department, Name AS Employee, Salary, RANK() OVER (Salary DESC PARTITION BY Department) AS RANKING
	FROM Employee E JOIN Department D ON
	(
		E.DepartmentId = D.DepartmentId

	) 
) AS T
WHERE RANKING <= 3