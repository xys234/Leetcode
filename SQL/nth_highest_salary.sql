-- (Medium) 177. Nth Highest Salary
-- Write a SQL query to get the nth highest salary from the Employee table.
-- 
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.
-- 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      --  Write your MySQL query statement below.
	  
	  SELECT Salary
	  FROM Employee
	  ORDER BY Salary DESC
	  LIMIT 1 OFFSET (N - 1)
	  
	  
      
  );
END



CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
     -- # Write your MySQL query statement below.
     SELECT MAX(Salary) 
            FROM Employee Emp1
            WHERE (N-1) = ( 
                 SELECT COUNT(DISTINCT(Emp2.Salary))
                        FROM Employee Emp2
                        WHERE Emp2.Salary > Emp1.Salary)
  );
END