module PreParcial(
    primo,
    primos
) where

primo :: Integer -> Bool
primo numero = length([x | x <- [2..numero-1], mod numero x == 0]) == 0

primos :: Integer -> [Integer] 
primos lista = [x | x <- [2..lista], primo x]

    