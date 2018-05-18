/*
(Medium) 178. Rank Scores
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. 
Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+


*/

-----------  MySQL ATTEMPT: STRONGER SOLUTION -------------- 

SELECT Score, (@rowid := @rowid + 1) as rowid,
(CASE 
	WHEN @prev = Score 	THEN @rank
	WHEN @prev := Score	THEN @rank := @rank + 1
 END
) AS Dense_Rank, 																-- Two kinds of ranks
@curRank := IF(@prevVal=Score, @curRank, @rowid) AS rank,						-- Two kinds of ranks
@prevVal:=Score
FROM Scores, (SELECT @rowid := 0, @rank := 0, @prev := NULL, @curRank := 0) r
ORDER BY Score DESC

-----------  MySQL ATTEMPT: REQUIRED OUTPUTS ONLY -------------- 
SELECT Score,
ROUND(CAST( (CASE 
	WHEN @prev = Score 	THEN @rank 
	WHEN @prev := Score	THEN @rank := @rank + 1
 END
) AS SIGNED), 0) AS Rank 																
FROM Scores, (SELECT @rank := 0, @prev := NULL) r
ORDER BY Score DESC


-----------  MySQL SOLUTION --------------
SELECT Score,  
      @rank := @rank + (@prevScore <> @prevScore := Score) Rank
  FROM Scores,  
      (SELECT @rank := 0, @prevScore := -1) init
  ORDER BY Score desc  

--- To understand the expression in the parenthesis, consider the following query
--- The Score table has 2 records (ID, Score) ~ [(1,0), (2,3.65)]

--- The results are 

--@prevScore	@prevScore <> @prevScore := Score	@prevScore	Score
--			-1									1			0		0
--			0									1			3.65	3.65
-- Takeaways:
-- 1. The select components are executed from left to right,
-- 2. The assignment occurs first. But the value of the variable is not updated until the next statament. This is why the comparison turns out to be true.  


SELECT @prevScore, @prevScore <> @prevScore := Score, @prevScore, Score
  FROM Scores,  
      (SELECT @rank := 0, @prevScore := -1.0) init