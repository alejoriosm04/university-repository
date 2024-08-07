import System.IO  
import Control.Monad

main = do  
        let listaTokens = []
        putStrLn "Nombre del archivo a leer? "
        archivo <- getLine
        conectorArchivo <- openFile archivo ReadMode
        contenido <- hGetContents conectorArchivo
        let token = words contenido
            listaTokens = token
        print listaTokens
        hClose conectorArchivo