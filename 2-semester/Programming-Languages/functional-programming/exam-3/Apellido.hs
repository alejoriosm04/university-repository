import Data.Char

main = do
    putStrLn "Cual es tu nombre?"
    nombre <- getLine
    putStrLn "Cual es tu primer apellido?"
    primerApellido <- getLine
    putStrLn "Cual es tu segundo apellido?"
    segundoApellido <- getLine
    let nombreMayusculas = map toUpper nombre
    let primerApellidoMayusculas = map toUpper primerApellido
    let segundoApellidoMayusculas = map toUpper segundoApellido
    putStrLn $ "Hola " ++ nombreMayusculas ++ " " ++ primerApellidoMayusculas ++ " " ++ segundoApellidoMayusculas ++ ", no te estoy reganando!!!"