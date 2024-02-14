-- lists all shows and genres linked to that show
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN hbtn_0d_tvshows.tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, genre ASC;
