/* Write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.

    Your query should output a table with a single column for the name of each person.
    People with the same birth year may be listed in any order.
    No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.
    If a person appeared in more than one movie in 2004, they should only appear in your results once. */ 

SELECT DISTINCT p.name
FROM people P, movies M, stars S
WHERE P.id = S.person_id AND M.id = S.movie_id
AND m.year = 2004
ORDER BY p.birth


/* Write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.

    Your query should output a table with a single column for the name of each person. */ 

SELECT director_names FROM
(SELECT distinct directors.person_id, people.name AS director_names
FROM people JOIN (directors JOIN ratings  ON directors.movie_id = ratings.movie_id) ON people.id = directors.person_id
WHERE rating >= 9.0)


/* Write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.

    Your query should output a table with a single column for the title of each movie.
    You may assume that there is only one person in the database with the name Chadwick Boseman. */ 

SELECT DISTINCT M.title
FROM movies M, people P, ratings R, stars S
WHERE M.id = R.movie_id AND P.id = S.person_id AND M.id = S.movie_id
AND P.name = "Chadwick Boseman"
ORDER BY rating DESC
LIMIT 5;


/* Write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.

    Your query should output a table with a single column for the title of each movie.
    You may assume that there is only one person in the database with the name Johnny Depp.
    You may assume that there is only one person in the database with the name Helena Bonham Carter. */ 

SELECT M.title
FROM movies M, people P1, people P2, stars S1, stars S2
WHERE  P1.id = S1.person_id AND P2.id = S2.person_id AND M.id = S1.movie_id AND M.id = S2.movie_id
AND P1.name = "Johnny Depp" AND P2.name = "Helena Bonham Carter";


/* Write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.

    Your query should output a table with a single column for the name of each person.
    There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
    Kevin Bacon himself should not be included in the resulting list. */ 
    
SELECT p2.name
FROM people P1, people P2, movies M, stars S1, Stars S2
WHERE  P1.id = S1.person_id AND P2.id = S2.person_id AND M.id = S1.movie_id AND M.id = S2.movie_id
AND P1.name = 'Kevin Bacon' AND P1.birth = '1958' AND P2.name != 'Kevin Bacon' and P2.id != '1958';