import Text.Printf

compra :: Int -> Int -> Int -> Double
compra precio cantidad iva
  | cantidad >= 5 = (fromIntegral precio) * (fromIntegral cantidad) * 0.75 * 0.81
  | otherwise = (fromIntegral precio) * (fromIntegral cantidad) * 0.81
  

main = do
       putStrLn "Ingrese el precio del producto: "
       textoPrecio <- getLine
       putStrLn "Ingrese la cantidad: " 
       textoCantidad <- getLine
       let iva = 19 
       let valorPrecio = (read textoPrecio :: Int)
       let valorCantidad = (read textoCantidad :: Int)
       printf "Valor compra: $ %f" $ compra valorPrecio valorCantidad iva