-- lists all shows, and all genres linked to that show from the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genre.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;