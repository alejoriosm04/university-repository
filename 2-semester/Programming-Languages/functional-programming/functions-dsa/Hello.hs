import Text.Printf
import PreParcial


factorial :: Integer -> Integer
factorial x = if x == 0 then 1 else x * factorial x-1

medio :: Int -> Int -> Int -> Int
medio x y z = if (x > y) && (y > z)  then y else medio z x y

main :: IO()
main = do
    print(primo 8)