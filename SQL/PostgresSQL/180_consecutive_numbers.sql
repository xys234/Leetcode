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
insert into Logs (Id, Num) values ('2', '1');
insert into Logs (Id, Num) values ('3', '1');
insert into Logs (Id, Num) values ('4', '2');
insert into Logs (Id, Num) values ('5', '1');
insert into Logs (Id, Num) values ('6', '2');
insert into Logs (Id, Num) values ('7', '2');

-- Solution 1 -- Window Function
-- https://dba.stackexchange.com/questions/212713/can-i-calculate-row-number-for-only-consecutive-records

WITH _cte
AS (
    SELECT *
        , Id - ROW_NUMBER() OVER (
                PARTITION BY Num ORDER BY Id
                ) AS grp
    FROM Logs
    )
   ,AddedRn    --add a row number for each entry in the group
AS (
    SELECT *
        ,ROW_NUMBER() OVER (
            PARTITION BY grp ORDER BY Id
            ) AS rn
    FROM _cte
    ), cte2 AS (
SELECT Id, Num, grp, rn as SeqWithinGroup    
FROM AddedRn
)
SELECT Num
FROM cte2
WHERE rn >= 3


