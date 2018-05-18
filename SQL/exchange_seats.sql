/*

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.
Mary wants to change seats for the adjacent students.
Can you write a SQL query to output the result for Mary?
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+



*/

-----------  MySQL ATTEMPT: ACCEPTED -------------- 

SELECT S1.id, (

CASE
	WHEN S1.id % 2 <> 0 AND S3.id IS NOT NULL THEN S3.student
	WHEN S1.id % 2 <> 0 AND S3.id IS NULL THEN S1.student
	WHEN S1.id % 2 = 0 THEN S2.student
END

) AS student 
FROM seat S1 LEFT JOIN seat S2 ON
(
  S1.id - S2.id = 1
) LEFT JOIN seat S3 ON 
(
	S1.id + 1 = S3.id
)
ORDER BY S1.id