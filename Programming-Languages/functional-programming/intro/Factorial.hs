import Text.Printf

-- funcion por patrones
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n*factorial(n-1)

-- funcion para calcular el perimetro de una circunferencia
circunferenciaP :: Float -> Float
circunferenciaP r = 2 * pi * r

pruebaFactorial x = printf "%d! = %d \n" x $ factorial x
pruebaCircunferenciaP r = printf "(%f) = %f \n" r $ circunferenciaP r

main :: IO ()
main = do
    --- pruebaFactorial 5
    mapM_ pruebaFactorial [1..20]
    mapM_ pruebaCircunferenciaP [1..10]
    