import Text.Printf

readInt :: String -> Int
readInt = read

main = do
    putStrLn "Hola, como te llamas?"
    nombre <- getLine
    putStrLn "En que año naciste?"
    nacimiento <- getLine

    putStrLn ("Que alegria " ++ nombre ++ ", eres un crack!")
    printf "En el 2022 tienes esta edad: %i" $ 2022 - readInt nacimiento