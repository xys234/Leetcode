-- (Hard) 601. Human Traffic of Stadium
-- X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, date, people
-- 
-- Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).
-- 
-- For example, the table stadium:
-- +------+------------+-----------+
-- | id   | date       | people    |
-- +------+------------+-----------+
-- | 1    | 2017-01-01 | 10        |
-- | 2    | 2017-01-02 | 109       |
-- | 3    | 2017-01-03 | 150       |
-- | 4    | 2017-01-04 | 99        |
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- For the sample data above, the output is:
-- 
-- +------+------------+-----------+
-- | id   | date       | people    |
-- +------+------------+-----------+
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- Note:
-- Each day only have one row record, and the dates are increasing with id increasing.


-----------  MySQL ATTEMPT --------------

SELECT s1.id AS id_1, s1.date AS date_1, s1.people AS people_1,
s2.id AS id_2, s2.date AS date_2, s1.people AS people_2,
s3.id AS id_3, s3.date AS date_3, s1.people AS people_3
FROM stadium s1 JOIN stadium s2 ON 
(
	DATEDIFF(s2.date, s1.date) = 1
) JOIN stadium s3 ON
(
	DATEDIFF(s3.date, s2.date) = 1
)
WHERE s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100


-----------  MySQL ANSWER --------------

SELECT DISTINCT d.* 
FROM (
	SELECT a.id 
	FROM stadium a, stadium b, stadium c 
	WHERE b.id-a.id=1 AND c.id - b.id=1 AND a.people>=100 AND b.people>=100 AND c.people>=100
) x, stadium d 
WHERE x.id<=d.id AND x.id+2>=d.id;
