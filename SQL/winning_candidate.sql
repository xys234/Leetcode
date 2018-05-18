/*

Table: Candidate

+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+  
Table: Vote

+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id is the auto-increment primary key,
CandidateId is the id appeared in Candidate table.
Write a sql to find the name of the winning candidate, the above example will return the winner B.

+------+
| Name |
+------+
| B    |
+------+
Notes:
You may assume there is no tie, in other words there will be at most one winning candidate.



*/

/* --------------  ATTEMPT ---------------- */

SELECT Name 
FROM Candidate
WHERE id = 
(
	SELECT CandidateId
	FROM 
	(
		SELECT CandidateId, COUNT(id) AS Votes
		FROM Vote
		GROUP BY CandidateId
	) v1
	WHERE Votes = 
	(
		SELECT MAX(Votes) 
		FROM 
		(
			(
				SELECT CandidateId, COUNT(id) AS Votes
				FROM Vote
				GROUP BY CandidateId
			) v2
		)
	)
)




/* --------------  SQL Fiddle Test Case ---------------- */
CREATE TABLE Candidate 
(
  id INT,
  Name VARCHAR(2)
);

CREATE TABLE Vote
(
  id INT,
  CandidateId INT
  );

INSERT INTO Candidate(id, Name) 
VALUES (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E');

INSERT INTO Vote(id, CandidateId) 
VALUES (1, 2), (2, 4), (3, 3), (4, 2), (5, 5);



/* ---------- Solution ---------------- */

SELECT
    name AS Name
FROM
    Candidate
        JOIN
    (SELECT
        Candidateid
    FROM
        Vote
    GROUP BY Candidateid
    ORDER BY COUNT(*) DESC
    LIMIT 1) AS Winner
WHERE
    Candidate.id = Winner.Candidateid
;
