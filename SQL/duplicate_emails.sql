/*

182. Duplicate Emails

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.



*/


-----------  MySQL ATTEMPT-1: ACCEPTED --------------

SELECT DISTINCT P1.Email
FROM Person P1 JOIN Person P2 ON
(
	P1.Email = P2.Email AND P1.Id <> P2.Id
)
WHERE P2.Email IS NOT NULL


-----------  MySQL ATTEMPT-2: ACCEPTED --------------

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Id) = 1