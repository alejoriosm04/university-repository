import Data.Char
import System.IO

main :: IO ()
main = do
    -- Function to read a file and convert it content into Upper Case
    -- contents <- getContents
    -- putStr (map toUpper contents)

    -- Read a file and print it content
    contents <- readFile "file.txt"
    putStrLn contents

    -- Write new content in a file
    putStrLn "Escribe el contenido a escribir: "
    contents1 <- getLine
    writeFile "archivo.txt" contents1

    -- Append new content in a file
    putStrLn "Escribe la nueva TO-DO: "
    todoItem <- getLine
    appendFile "todo.txt" (todoItem ++ "\n")