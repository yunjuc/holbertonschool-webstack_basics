-- query all cities in a state
SELECT cities.id, cities.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
WHERE states.name = "California"
ORDER BY cities.id ASC;
