/*
Given a table salary, such as the one below, that has m=male and f=female values. 
Swap all f and m values (i.e., change all f values to m and vice versa) with a single update query and no intermediate temp table.
For example:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
After running your query, the above salary table should have the following rows:
| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |

*/


-- Swap salaries
UPDATE salary s1 LEFT JOIN salary s2 ON 
(
	s1.id + 1 = s2.id 
) LEFT JOIN salary s3 ON 
(
	s1.id - 1 = s3.id
)
SET s1.salary = 
CASE 
	WHEN s1.sex = "m" THEN s2.salary
	WHEN s1.sex = "f" THEN s3.salary
END


-- Update sexes

UPDATE salary
SET sex = 
CASE 
	WHEN sex = "m" THEN "f"
	WHEN sex = "f" THEN "m"
END