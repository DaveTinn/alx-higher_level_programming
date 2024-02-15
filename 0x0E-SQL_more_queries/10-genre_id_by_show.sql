-- Import the database dump from hbtn_0d_tvshows
-- Lists all shows contained in 'hbtn_0d_tvshows' that have atleast one genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_shows_genres.genre_id
	FROM tv_shows
	INNER JOIN tv_shows_genres
	ON tv_shows.id = tv_shows_genres.show_id
	ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
