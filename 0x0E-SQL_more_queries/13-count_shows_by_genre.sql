-- lists all genres from hbtn_0d_tvshows and displays number of shows linked to each
SELECT
    g.genre AS genre,
    COUNT(tg.tv_show_id) AS number_of_shows
FROM
    hbtn_0d_tvshows.tv_show_genres tg
JOIN
    hbtn_0d_tvshows.genres g ON tg.genre_id = g.id
GROUP BY
    g.genre
ORDER BY
    number_of_shows DESC;
