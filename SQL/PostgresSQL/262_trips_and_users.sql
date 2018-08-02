/*


The Trips table holds all taxi trips. Each trip has a unique Id, 
while Client_Id and Driver_Id are both foreign keys to the Users_Id at the Users table. 
Status is an ENUM type of (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’).

+----+-----------+-----------+---------+--------------------+----------+
| Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
+----+-----------+-----------+---------+--------------------+----------+
| 1  |     1     |    10     |    1    |     completed      |2013-10-01|
| 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
| 3  |     3     |    12     |    6    |     completed      |2013-10-01|
| 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
| 5  |     1     |    10     |    1    |     completed      |2013-10-02|
| 6  |     2     |    11     |    6    |     completed      |2013-10-02|
| 7  |     3     |    12     |    6    |     completed      |2013-10-02|
| 8  |     2     |    12     |    12   |     completed      |2013-10-03|
| 9  |     3     |    10     |    12   |     completed      |2013-10-03| 
| 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
+----+-----------+-----------+---------+--------------------+----------+
The Users table holds all users. Each user has an unique Users_Id, 
and Role is an ENUM type of (‘client’, ‘driver’, ‘partner’).

+----------+--------+--------+
| Users_Id | Banned |  Role  |
+----------+--------+--------+
|    1     |   No   | client |
|    2     |   Yes  | client |
|    3     |   No   | client |
|    4     |   No   | client |
|    10    |   No   | driver |
|    11    |   No   | driver |
|    12    |   No   | driver |
|    13    |   No   | driver |
+----------+--------+--------+
Write a SQL query to find the cancellation rate of requests made by unbanned users between Oct 1, 2013 and Oct 3, 2013. 
For the above tables, your SQL query should return the following rows with the cancellation rate being rounded to two decimal places.

+------------+-------------------+
|     Day    | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 |       0.33        |
| 2013-10-02 |       0.00        |
| 2013-10-03 |       0.50        |
+------------+-------------------+


*/



-- Solution: Not accepted; Time-out; DBFiddle produced correct outputs

WITH Trips2 AS (
	SELECT Id, Client_Id, Driver_Id, City_Id, Status, Request_at, S.Banned AS User_banned
	FROM Trips T INNER JOIN Users U ON (
		T.Client_Id = U.Users_Id
	
	)
), Trips_Requested AS
(
	SELECT Request_at, COUNT(Status) AS Trips_Requested
	FROM Trips2
	WHERE User_banned LIKE 'No'
	GROUP BY Request_at
), Trips_Completed AS (
	SELECT Request_at, COUNT(Status) AS Trips_Requested
	FROM Trips2
	WHERE User_banned LIKE 'No' AND Status LIKE 'completed'
	GROUP BY Request_at
	
)
SELECT R.Request_at AS Day, ROUND(1.0 - Trips_Completed / Trips_Requested, 2) AS Cancellation_Rate
FROM Trips_Requested R JOIN Trips_Completed C ON (

	R.Request_at = C.Request_at
)
ORDER BY R.Request_at


-- Solution 2: Accepted

SELECT Request_at AS Day, ROUND(1.0 - (SUM(CASE WHEN Status LIKE 'completed' THEN 1 ELSE 0 END)*1.0 / COUNT(Status)), 2) AS [Cancellation Rate]
FROM Trips T INNER JOIN Users U ON (
		T.Client_Id = U.Users_Id	
)
WHERE Banned LIKE 'No' AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at
ORDER BY Request_at
 






