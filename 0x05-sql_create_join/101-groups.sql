-- computer the number of the same score
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
