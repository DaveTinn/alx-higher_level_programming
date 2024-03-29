-- Import the database dump from hbtn_0d_tvshows
-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
	-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
	-- Each record should display: tv_genres.name
	-- Results must be sorted in ascending order by the genre name
	-- You can use a maximum of two SELECT statement
	-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS dexter_genre AS (
	SELECT tv_genres.id, tv_genres.name
	FROM tv_genres
	INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter');
	SELECT tv_genres.name
	FROM tv_genres
	LEFT JOIN dexter_genre ON dexter_genre.id = tv_genres.id
	WHERE dexter_genre.id IS NULL
ORDER BY tv_genres.name ASC;
