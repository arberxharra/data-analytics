/*
a) The actor table contains actor IDs, first names, last names, and the last updated date.

b) The film table contains film IDs, titles, descriptions, release years, language IDs, rental information, ratings, and special features.

c) The film_actor table contains both actor_id and film_id.

d) The rental table contains rental IDs, rental dates, inventory IDs, customer IDs, return dates, and staff IDs. It is hard to read because it uses IDs instead of names.

e) The inventory table contains inventory IDs, film IDs, store IDs, and last updated dates. It tracks which copies of films belong to each store.

f) To find the names of films rented on a specific date, I would use the rental, inventory, and film tables. The rental table connects to inventory through inventory_id, and inventory connects to film through film_id. This allows me to find film titles based on rental dates.
*/

USE sakila;

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;