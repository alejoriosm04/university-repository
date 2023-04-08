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