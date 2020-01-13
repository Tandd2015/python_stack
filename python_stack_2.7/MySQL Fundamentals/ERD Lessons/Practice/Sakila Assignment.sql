-- The saklia database that was downloaded from the learning platform was no where near exstensive as what the reference diagram in the PNG file was so the
-- expected results and the SQL query anwsers in the solution do not match exactly with my anwsers because of the missing information of the sakila database
-- caused my SQL answer queries to have errors and not run for some of the questions asked on the assignment.

--  What query would you run to get all the customers inside city_id = 312? Your query should returm customer first name, last name, email, and address.
SELECT city.city_id , city.city, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.customer_id = address.address_id
JOIN city ON address.city_id =  city.city_id
WHERE city.city_id = 312;

-- What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'genre'
FROM film
JOIN category ON film.film_id = category.category_id
WHERE category.category_id = 5;

-- What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.
 


