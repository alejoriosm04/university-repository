-- Select the data from the table
SELECT * FROM people;

-- Select the data from the view
SELECT * FROM v_madrid_customers;

-- Select specific columns from the table
SELECT first_name, last_name FROM people;

-- Insert data into the table
INSERT INTO people (first_name, last_name, city)
VALUES ('John', 'Doe', 'Madrid');

-- Update data in the table
UPDATE people
SET city = 'Barcelona'
WHERE city = 'Madrid';

-- Delete data from the table
DELETE FROM people
WHERE city = 'Barcelona';

-- Summary
SELECT * FROM students;

INSERT INTO students (nombre, apellido, edad, correo_electronico, telefono) 
VALUES ("Alexis", "Araujo", 33, "alexis@gmail.com", "777-1234");

DELETE FROM students 
WHERE id = 1;

UPDATE students 
SET edad = 55 
WHERE id = 2;