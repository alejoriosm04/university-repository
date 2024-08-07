{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Eta reduce" #-}
import Text.Printf
--module Prueba where

--Funciones prefijas: -(-2)
--Funciones infijas: 2 + 2
--Funciones postfija 2**

--funcion por patrones
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n*factorial(n-1)

pruebaFAc x = printf "%d! = %d\n" x $ factorial x

circulo :: Float -> Float
circulo x = 2*pi*x

pruebaCir x = printf "De radio %f, su perimetro es %f\n" x $ circulo x

divisionPrefija :: Int -> Int -> Int
divisionPrefija x y = div x y 

divisionInfija :: Int -> Int -> Int
divisionInfija x y = x `div` y 

pruebaDiv x y = printf "%d sobre %d = %d\n" x y $ divisionInfija x y

main :: IO()
main = do
    --mapM_ pruebaCir [1..20]
    pruebaDiv 15 5