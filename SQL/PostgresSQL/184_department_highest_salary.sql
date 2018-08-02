/*

184. Department Highest Salary 

The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. 
For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+



*/

-- Solution 1: Window Function
SELECT Employee 
SELECT DepartmentId, MAX(Salary) AS MaxSalary
FROM Employee
GROUP BY DepartmentId


-- Solution 2: Subquery

SELECT D.Name AS Department, E.Name AS Employee, Salary
FROM Employee E JOIN Department D ON (
	E.DepartmentId = D.Id
)
WHERE Salary = (
	SELECT Max(Salary)
	FROM Employee
	WHERE E.DepartmentId = DepartmentId
)
ORDER BY D.Name