-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
