{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant return" #-}

import Control.Monad

main = do
    listaLenguajes <- forM [1,2,3,4,5] (\posicionLenguaje -> do
        putStrLn $ "Escriba el nombre de lenguaje de programacion de mejor a peor (Los 5 mejores):  " ++ show posicionLenguaje ++ "?"
        lenguaje <- getLine
        return lenguaje)
    putStrLn "Su orden de lengajes de programacion es de mejor a peor: "
    mapM putStrLn listaLenguajes