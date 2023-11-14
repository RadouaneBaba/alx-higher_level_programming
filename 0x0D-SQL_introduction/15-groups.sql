-- script that lists the number of records with the same score in the table second_table
SELECT score, COUNT(score) FROM second_TABLE GROUP BY score ORDER BY COUNT(score) DESC;
