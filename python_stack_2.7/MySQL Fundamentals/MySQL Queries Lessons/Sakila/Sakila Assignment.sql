-- What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.

SELECT address.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address
FROM customer 
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE city.city_id = 312;

-- What query would you run to get all comedy films? Your query would return film title, description, release year, rating, special features and genre.

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'genre'
FROM film 
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.category_id = 5;

-- What query would you run to get all the films joined by actor_id=5? Your query shoud return the film title, description and release year.

SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

-- What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address.

SELECT store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM store
JOIN customer ON customer.store_id = store.store_id
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE store.store_id = 1 AND city.city_id IN (1, 42, 312, 459);

-- What query would you run to get all the films with a rating = G and special feature = behind the scenes, joined by actor_id = 15? Your query shoud return the film title, description, release year, rate and special feature.

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.rating = 'G' AND film.special_features LIKE '%Behind the Scenes%' AND actor.actor_id = 15;

-- What query would you run to get all the actors that joined in the film_id = 369? Your query should return the first_name, last name and last_update of the actors.

SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

-- What query would you run to get all drama films with a rental rate of 2.99 ? Your query should return film title, description, release year, rating, special features and genre.f

SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Drama' AND film.rental_rate = 2.99;

-- What query would you run to get all the action films joined by SANDRA KILMER. Your query should return film title, description, release year, rating, special features, genre and actor's first name and last name.

SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name, film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'Action' AND CONCAT(actor.first_name, ' ', actor.last_name) = 'SANDRA KILMER';

