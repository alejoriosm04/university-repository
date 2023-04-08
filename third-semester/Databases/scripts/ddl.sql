-- Create a Schema or a Database
CREATE DATABASE test_db;
-- Set as default database
USE DATABASE test_db;

-- Create a Table
CREATE TABLE test_table (
    id INT NOT NULL AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    --Accept NULL values
    age INT NULL,
    -- Set a Primary Key
    PRIMARY KEY (id)
);

-- Another way to create a Table
CREATE TABLE people (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    last_name VARCHAR(255) NULL,
    first_name VARCHAR(255) NULL,
    address VARCHAR(255) NULL,
    city VARCHAR(255) NULL
);

-- Create a View
CREATE VIEW people_view AS
SELECT
    last_name,
    first_name,
    city
FROM
    people
WHERE
    city = 'Medellin';

-- Alter a Table
ALTER TABLE people
ADD COLUMN email VARCHAR(255) NULL;

ALTER TABLE people
ALTER COLUMN email VARCHAR(255) NOT NULL;

ALTER TABLE people
DROP COLUMN email;

-- Drop a Table
DROP TABLE people;

-- Drop a Database
DROP DATABASE test_db;

-- Drop a View
DROP VIEW people_view;

-- Summary
CREATE VIEW v_madrid_customers AS
SELECT
  person_id,
  last_name,
  first_name
FROM people
WHERE
  city = 'Madrid';

SELECT * FROM v_madrid_customers;

ALTER TABLE people
ADD COLUMN date_of_birth DATE;

ALTER TABLE people
DROP COLUMN address;