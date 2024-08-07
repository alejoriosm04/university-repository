<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solicitar Nombre</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        label {
            font-size: 1rem;
            color: #555;
        }
        input[type="text"] {
            padding: 10px;
            font-size: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        input[type="submit"] {
            padding: 10px;
            font-size: 1rem;
            color: #fff;
            background-color: #28a745;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        .message {
            margin-top: 20px;
            text-align: center;
            font-size: 1rem;
        }
        .success {
            color: #28a745;
        }
        .error {
            color: #dc3545;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Ingrese su nombre</h2>
        <form action="" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            <input type="submit" value="Guardar">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Asumimos que esta en el servidor local
            $servername = "localhost";
            $username = "root";
            $password = "";
            $dbname = "nombreDB";

            // Nueva conexión a la base de datos usando mysqli
            $conn = new mysqli($servername, $username, $password, $dbname);

            // Verificar conexión y usamos die para cerrar (tambien se puede exit)
            if ($conn->connect_error) {
                die("<p class='message error'>Conexión fallida: " . $conn->connect_error . "</p>");
            }

            // Declaramos la variables nombre
            // y obtenemos el valor del input
            $nombre = $_POST['nombre'];

            // Crea la consulta SQL para insertar el nombre en la tabla nombres
            $sql = "INSERT INTO nombres (nombre) VALUES ('$nombre')";

            if ($conn->query($sql) === TRUE) {
                echo "<p class='message success'>Nombre guardado exitosamente</p>";
            } else {
                echo "<p class='message error'>Error: " . $sql . "<br>" . $conn->error . "</p>";
            }

            $conn->close();
        }
        ?>
    </div>
</body>
</html>
