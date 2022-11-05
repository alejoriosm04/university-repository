# Parcial 3 - Programación Funcional en Haskell
## Pregunta 1
```haskell
import Text.Printf

readInt :: String -> Int
readInt = read

main = do
    putStrLn "Hola, como te llamas?"
    nombre <- getLine
    putStrLn "Que edad tienes?"
    edad <- getLine

    putStrLn ("Que alegria " ++ nombre ++ ", eres un crack!")
    printf "En 10 años tendras: %i" $ readInt edad + 10
```

### Respuesta
Describe aquí: - Importamos la librería de Text.Printf para poder cambiar mas adelante el formato de impresión. Posterior, se crea una función readInt, que recibe un String y retornará un entero, esto lo hacemos con la acción "read" de Haskell, que nos permite hacer esto. A continuación, sigue el bloque de función main, el punto de entrada principal. En este, imprimimos un String que indica que debemos de meter en consola, en este caso, el nombre. Luego, lo mismo pero nos pide la edad. Finalmente, se hace un output en consola, concatenando el nombre con una frase de motivación y posterior, se hace un printf que hace la conversión de formato, ya que incluiremos una operación con enteros. Se envia la edad a la función "readInt", le sumamos 10 y lo concatenamos con un String, enviandolo a través del cambio de formato.

## Pregunta 2
```haskell
import Data.Char

main = do
    putStrLn "Cual es tu nombre?"
    nombre <- getLine
    putStrLn "Cual es tu apellido?"
    apellido <- getLine
    let nombreMayusculas = map toUpper nombre
    let apellidoMayusculas = map toUpper apellido
    putStrLn $ "Hola " ++ nombreMayusculas ++ " " ++ apellidoMayusculas ++ ", no te estoy regañando!!!"
```

### Respuesta
Describe aquí: Importamos la librería Data.Char que nos permitirá manipular con datos de tipo Char. Inicia el bloque de código de la función main. Imprimos preguntando al usuario por el nombre, se lo pedimos con getLine. Lo mismo con el apellido, almacenamos ambos valores en sus respectivas variables. Declaramos dos variables que guardarán el nombre en mayúsculas. En estas variables, enviamos el String almacenado de nombre y apellido, en un mapa de Chars y los pasamos a la función toUpper que los convierte en mayusculas. Finalmente, concatenamos estas variables con un String, usando putStrLn, donde el nombre y el apellido se veran en mayusculas.

## Pregunta 3
```haskell
 --Para terminar el mundo espejo, simplemente presione <<ENTER>>

mundoEspejo :: String -> String
mundoEspejo = unwords . map reverse . words

main = do
    linea <- getLine
    if null linea
        then return ()
        else do
            putStrLn $ "mundo espejo: " ++ mundoEspejo linea
            main
```

### Respuesta
Describe aquí: Indicamos en un comentario inicial como finalizar el programa. Creamos una función llamada mundoEspejo, la cual recibe un String y retorna un String también. En esta función, enviamos lo que recibimos en este caso con words, para poder trabajar con Chars en un mapa. Al tener en un mapa de caracteres el string original, lo invertimos, y le volvemos a aplicar unwords para poder convertirlo en un String normal de nuevo y retornarlo. Posterior, sigue el bloque de código main, pedimos una linea al usuario con getLine, si esta linea esta vacía se acaba el programa, ya que es un ciclo infinito hasta que esto no ocurra. Si no es así, entonces enviamos esta línea ingresada por el usuario a mundoEspejo y la imprimimos en pantalla concatenada con putStrLn, ya invertida. Se vuelve a llamar la función main para cumplir con este ciclo infinito centinela.

## Pregunta 4
```haskell
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant return" #-}

import Control.Monad

main = do
    listaLenguajes <- forM [1,2] (\idLenguaje -> do
        putStrLn $ "Escriba el nombre de lenguaje de programación en el orden:  " ++ show idLenguaje ++ "?"
        lenguaje <- getLine
        return lenguaje)
    putStrLn "Su orden de lengajes de programación es: "
    mapM putStrLn listaLenguajes
```

### Respuesta
Describe aquí: Importamos la librería para trabajar con Monadicos, ya que como tendremos dos listas en este programa, vamos a trabajar con cada elemento por separado, esto son monadicos por definición. En la función principal main, llamamos la variable listaLenguajes la cual realiza: para una lista definida de 1 a 2, llamamos a cada elemento por indiividual, y los enviamos a otra función, llamada idLenguaje, esta función se ejecuta inmediatamente y realiza lo siguiente, pregunta al usuario por pantalla por el nombre del Lenguaje de Programación, correspondiente a este id, todo esto concatenado en un putStrLn, se almacena la entrada con getLine en una variable lenguaje y se devuelve esta variable para que sea almacenada en la listaLenguaje. Cuando termine de evaluar cada elemento de forma monadica, imprime la lista en el orden respectivo con mapM que también trabaja cada elemento por separado, por lo tanto, lo imprime por separado en orden.

## Pregunta 5
```haskell
import Text.Printf

compra :: Int -> Int -> Int -> Double
compra precio cantidad iva =
    let valor_compra = (fromIntegral precio) * (fromIntegral cantidad)
        valor_iva = valor_compra * (fromIntegral iva) / 100
    in  valor_iva + valor_compra

main = do
       putStrLn "Ingrese el precio del producto: "
       textoPrecio <- getLine
       putStrLn "Ingrese la cantidad: " 
       textoCantidad <- getLine
       let iva = 19 
       let valorPrecio = (read textoPrecio :: Int)
       let valorCantidad = (read textoCantidad :: Int)
       printf "Valor compra: $ %f" $ compra valorPrecio valorCantidad iva
```

### Respuesta
Describe aquí: De nuevo, se importa la librería para imprimir cambiando el formato en el caso que se necesite. Creamos una función "compra", la cual recibe 3 variables de tipo Entero y retorna una variable de tipo Double. Las 3 variables que se envian respectivamente son precio, cantidad e iva. Primero calculamos el valor de la compra sin iva, se hace la respectiva operación matemática. Luego, calculamos el iva de la compra sacandole el porcentaje y sumamos esto al valor total de la compra. Se retorna el valor de valor_compra. Posterior, se ejecuta el bloque main, donde se le pregunta al usuario por el precio y la cantidad, cada valor con getLine y almacenados en sus respectivas variables, también declaramos el valor del iva, convertimos los valores recibidos por consola de precio y cantidad a enteros con "read", esta conversión almacena los valores en nuevas variables. Finalmente, se envian estas 3 variables a la función compra como se habia explicado, y se concatena el resultado que se produce en un printf que se encarga de realizar el formato para la impresión, recibiendo el valor_compra.

## Pregunta 1
```haskell
import System.IO  
import Control.Monad

main = do  
        let listaTokens = []
        putStrLn "Nombre del archivo a leer? "
        archivo <- getLine
        conectorArchivo <- openFile archivo ReadMode
        contenido <- hGetContents conectorArchivo
        let token = words contenido
            listaTokens = token
        print listaTokens
        hClose conectorArchivo   
```

### Respuesta
Describe aquí: Importamos libreria para manejar I/O desde el entorno de nuestro sistema local, es decir, para poder manejar archivos y también la librería que nos permite trabajar con monadicos. Posterior, el bloque de código main, declaramos una lista vacía, que almacenará los tokens del archivo que leamos. Preguntamos al usuario por el nombre del archivo que desea leer con getLine y se almacena en una variable archivo. Enviamos esta variable a la acción openFile e indicamos que será en modo de lectura con ReadMode, de esta forma, realizamos el enlace entre programa y archivo. Consecutivamente, con esta conexión del archivo, extraemos el contenido con hGetContents y almacenamos todo este contenido en una sola variable. Finalmente, creamos una variable que almacena token por token del contenido almacenado en "contenido" y estos tokens son añadidos a la lista de tokens. Se imprime esta lista en consola y se cierra el archivo para evitar cualquier error

Comente aquí que haria: Si el reto propuesto hace referencia a separar el código de Haskell línea por línea, el token seria cada vez que se encuentre un salto de línea con \n, para que la separación y el almacenamiento línea por línea se realiace a partir de esto. Basicamente sería el mismo proceso del código de analisis, solo sería necesario especificar el token de separación deseado en words cuando se realiza la separación.