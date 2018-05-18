/*

LeetCode 571. Find Median Given Frequency of Numbers

The Numbers table keeps the value of number and its frequency.

+----------+-------------+
|  Number  |  Frequency  |
+----------+-------------|
|  0       |  7          |
|  1       |  1          |
|  2       |  3          |
|  3       |  1          |
+----------+-------------+
In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

Write a query to find the median of all numbers and name the result as median.



*/


/* --------- ATTEMPT --------- */
/*

Construct a table
Number	Frequnecy	RunTotal	UpperId	LowerID
1		1			1			4		3
2		2			3			4		3
3		1			4			4		3
4		1			5			4		3
5		1			6			4		3

*/


/*----- ATTEMPT ------ */

SELECT AVG(t1.Number) AS Number
FROM
(
    SELECT Number, Frequency, (@runtotal := @runtotal + Frequency) AS RunTotal
    FROM Numbers, (SELECT @runtotal := 0) AS init
) t1
INNER JOIN 
(
	SELECT Number, 
	(
	  SELECT FLOOR((SUM(Frequency)+2)/2) 
	  FROM Numbers
	) AS UpperID,
	(
	  SELECT FLOOR((SUM(Frequency)+1)/2) 
	  FROM Numbers
	) AS LowerID
		FROM Numbers
) t2 ON
(
    t1.Number = t2.Number
)
WHERE t1.RunTotal = t2.UpperID OR t1.RunTotal = t2.LowerID








/* ------------ SOLUTION ------ */




/* SQL FIDDLE TEST CASE*/ 

CREATE TABLE Numbers 
(
  Number INT,
  Frequency INT
);

INSERT INTO Numbers(Number, Frequency) 
VALUES (0,5), (1,1), (2,3), (3,1);

