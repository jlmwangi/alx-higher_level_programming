-- uses hbtn_0d_tvshows database to list all genres of Dexter
SELECT tv_genres.name
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN hbtn_0d_tvshows.tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
