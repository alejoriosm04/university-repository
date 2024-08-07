# Simple PHP Form Application

This is a simple PHP application that collects a user's name through a form and stores it in a MySQL database.

## Requirements

- XAMPP (or any other server environment that supports PHP and MySQL)
- Web browser

## Setup Instructions

### 1. Start XAMPP

1. Open the XAMPP Control Panel.
2. Start the Apache and MySQL modules.

### 2. Create the Database

1. Open your web browser and go to `http://localhost/phpmyadmin`.
2. Create a new database named `nombreDB` by entering the name in the "Create database" field and clicking "Create".
3. Select the `nombreDB` database and go to the SQL tab.
4. Execute the following SQL code to create the `nombres` table:
    ```sql
    CREATE TABLE nombres (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL
    );
    ```

### 3. Run the Application

1. Place the `index.php` file in the root directory of your web server (e.g., `htdocs` if you are using XAMPP).
2. Open your web browser and go to `http://localhost/php-course/index.php`.
3. Enter a name in the form and click "Guardar".
4. The name will be stored in the `nombres` table of the `nombreDB` database.