-- list

SELECT g.name AS genre, count(s.genre_id) AS number_of_shows FROM tv_genres g JOIN tv_show_genres s ON id = genre_id
GROUP BY g.name
ORDER BY count(s.genre_id) DESC;