-- list all recoreds in a table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
