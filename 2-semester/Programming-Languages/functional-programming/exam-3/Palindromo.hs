mundoEspejo :: String -> String
mundoEspejo = unwords . map reverse . words

main = do
    linea <- getLine
    if null linea
        then return ()
        else do
          let espejo = mundoEspejo linea
          if espejo == linea
            then putStrLn "Es palindromo"
            else do
            putStrLn "No es palindromo"
          main