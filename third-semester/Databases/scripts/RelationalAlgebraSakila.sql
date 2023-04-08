SELECT
	first_name,
    last_name
FROM
	customer;
    
SELECT
	title,
	description
FROM
	film;
    
DESC FILM;

SELECT * FROM city;

DESC customer;

SELECT
	email,
	store_id
FROM customer
WHERE first_name = "Mary" and last_name = "Smith";

DESC rental;

SELECT
	rental_id,
    rental_date
FROM
	rental
WHERE
	return_date >= "2005-05-01 00:00:00" 
    AND 
    return_date <= "2005-05-31 00:00:00";
    
SELECT
	first_name,
    last_name
FROM
	customer
UNION
SELECT
	first_name,
	last_name
FROM
	actor;
    
SELECT
	customer_id
FROM
	customer
WHERE NOT EXISTS
(SELECT
	customer_id
FROM
	rental);
    
SELECT DISTINCT title
FROM film f INNER JOIN inventory i ON (f.film_id = i.film_id)
WHERE store_id = 1;

DESC store;
DESC inventory;

SELECT * FROM rental;

select rental_id, first_name, last_name
 from rental, customer
order by rental_id, first_name, last_name;

SELECT first_name, last_name, return_date
FROM rental INNER JOIN customer ON (rental.customer_id = customer.customer_id)
WHERE return_date >= "2005-05-01 00:00:00" 
    AND 
    return_date <= "2005-05-31 00:00:00";
    
DESC film_category;
DESC film;

SELECT title, name
FROM film INNER JOIN film_category USING(film_id)
INNER JOIN category USING(category_id)
ORDER BY film.film_id;

SELECT title, name
FROM film INNER JOIN film_category USING(film_id)
INNER JOIN category ON(category.category_id = film_category.category_id)
ORDER BY film.film_id;

SELECT name, title, description, release_year
FROM film INNER JOIN film_category USING(film_id)
INNER JOIN category USING(category_id);

Select c.name 'Category Name', 
 f.title 'Film Title', 
 f.description 'Film Description',
 f.release_year 'Release Year'
 from category c JOIN film_category fc ON c.category_id = fc.category_id 
 JOIN film f ON f.film_id = fc.film_id;
 
 SELECT customer_id AS "Cliente", COUNT(*) AS "Total Rentas"
 FROM rental
 GROUP BY customer_id
 ORDER BY customer_id;
 
  SELECT customer_id AS "Cliente", COUNT(*) AS "Total Rentas"
 FROM rental
 GROUP BY customer_id
HAVING COUNT(*) > 30;

SELECT customer_id AS "Cliente", AVG(amount) AS "Promedio Pagado"
FROM payment
GROUP BY customer_id
ORDER BY customer_id;