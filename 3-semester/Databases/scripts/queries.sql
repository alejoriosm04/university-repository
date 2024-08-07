-- Select some columns from the table and change the name of the columns
SELECT 
    first_name AS "First Name",
    last_name AS "Last Name",
    city AS "City"
FROM people;

-- Count the number of rows in the table
SELECT COUNT(*) FROM people;

-- Summary SELECT
SELECT * FROM cursos;
SELECT COUNT(*) AS "cantidad" FROM cursos;
SELECT
  nombre AS name,
  profe AS teacher,
  n_calificaciones AS n_reviews
FROM cursos;

-- Calculate the average of grades for each student
SELECT student_id, AVG(grade) AS average_grade
FROM grades
GROUP BY student_id;

-- Calculate total average grade
SELECT AVG(grade) AS total_average_grade
FROM grades;

-- Mostrar el promedio pagado por cada cliente en cada renta
SELECT customer_id, AVG(amount) AS "Promedio Pagado"
FROM payment
GROUP BY customer_id;

SELECT customer_id, rental_id, AVG(amount) AS "Promedio"
FROM payment
GROUP BY rental_id
HAVING Promedio > 2
ORDER BY customer_id, rental_id;


SELECT rental_id, AVG(amount) AS average_amount
FROM payment
GROUP BY rental_id;

SELECT * FROM payment
WHERE customer_id = 1
ORDER BY customer_id;