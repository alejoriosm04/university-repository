import Data.List
import Text.Printf

solvePN :: String -> Float
solvePN = head . foldl foldingFunction [] . words
    where   foldingFunction (x:y:ys) "*" = (x * y):ys
            foldingFunction (x:y:ys) "+" = (x + y):ys
            foldingFunction (x:y:ys) "-" = (y - x):ys
            foldingFunction (x:y:ys) "/" = (y / x):ys
            foldingFunction (x:y:ys) "^" = (y ** x):ys
            foldingFunction (x:xs) "ln" = (log x):xs
            foldingFunction (xs) "sum" = [sum xs]
            foldingFunction xs numberString = read numberString:xs

main :: IO ()
main = do
    putStrLn ""-------------------------------------------------------------------------------------------""
    putStrLn "Welcome to the Polish Notation Calculator."
    putStrLn "Please take into account the following recommendations:"
    putStrLn "- Each character, number or operator must be separated to each other by only ONE space."
    putStrLn "- At the moment, the calculator only accepts +, -, * and / , as mathematic operations."
    putStrLn "- Use the Sufix Polish Notation, the program at the moment, only works with this notation."
    putStrLn "We hope you enjoy this program. Soon we will add new features..."
    putStrLn "-------------------------------------------------------------------------------------------"

    putStrLn "Enter the expression to calculate (SUFIX NOTATION):"
    putStrLn "To close the program, press [ENTER]"
    expression <- getLine
    if null expression
        then return ()
        else do
            putStrLn "-------------------------------------------------------------------------------------------"
            printf "The answer is: %f \n" $ solvePN expression
            putStrLn "-------------------------------------------------------------------------------------------"
            main
