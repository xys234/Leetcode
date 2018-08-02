/*

180. Consecutive Numbers

Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+



*/

-- DDL

Create table If Not Exists Logs (Id int, Num int);
Truncate table Logs;
insert into Logs (Id, Num) values ('1', '1');
insert into Logs (Id, Num) values ('2', '2');
insert into Logs (Id, Num) values ('3', '1');
insert into Logs (Id, Num) values ('4', '1');
insert into Logs (Id, Num) values ('5', '1');
insert into Logs (Id, Num) values ('6', '2');
insert into Logs (Id, Num) values ('7', '2');

-- Solution 1 -- Window Function
-- https://dba.stackexchange.com/questions/198392/finding-gaps-and-islands-with-repeating-group-numbers
-- Takeaway: Lag function to identify group head and cumulative SUM to mark groups

WITH cte AS (

SELECT Id, Num, (CASE WHEN LAG(Num, 1) OVER (ORDER BY Id) IS NULL OR 
                 LAG(Num, 1) OVER (ORDER BY Id) <> Num THEN 1 ELSE 0 END) AS Head
FROM  Logs  
), grp AS (
  
 	SELECT Id, Num, Head, SUM(Head) OVER (ORDER BY Id) AS grp
    FROM cte
  
)  
SELECT DISTINCT num AS ConsecutiveNums
FROM grp
GROUP BY grp, num
HAVING COUNT(grp) >= 3


