# Homework 2
### Working with SQL data derived from from the MovieLens data. 

Created a database with the imported sql data (in psql)

Connected to the database via pg8000 in jupyter

Performed a variety of queries on the data using WHERE, ORDER BY, aggregation, GROUP BY, HAVING, COUNT() and JOIN in order to have the desired output. 

Order of queries matters! Sometimes SQL commands will not work if they are not run in a specific order.

For ex: ```
SELECT avg(rating), movie_title
FROM udata JOIN uitem ON item_id = movie_id
WHERE horror = 1
GROUP BY movie_title
HAVING count(rating) > 10
ORDER BY avg(rating)
LIMIT 10; ```

ORDER BY needs to come after all of the other statements in this SQL query or else an error occurs. 
