--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- each record should display: tv_genres.name - number_shows
-- don’t display a genre that doesn’t have any shows linked
-- results must be sorted in descending order by the number of shows linked
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command
-- genre id by show
SELECT tgs.name AS genre, COUNT(tg.genre_id) AS number_shows
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
LEFT JOIN tv_genres AS tgs
ON tg.genre_id = tgs.id
WHERE tg.genre_id IS NOT NULL
GROUP BY tgs.name ORDER BY number_shows DESC;
