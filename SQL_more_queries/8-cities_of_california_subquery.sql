-- Lists all the cities of 'California' state that can be found in the database

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
