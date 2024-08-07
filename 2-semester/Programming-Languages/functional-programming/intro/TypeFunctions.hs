import Text.Printf

-- Funciones por patrones
suerte:: (Integral variable) => variable -> String
suerte 7 = "Genial es 7, es suerte :)"
suerte 13 = "Mejor no lo digo"
suerte variable = "Upsss, sigue intentando"

-- Funciones por guardas
imc :: (RealFloat variable) => variable -> variable -> String
imc peso altura
    | peso / altura^2 <= 18.5 = "Eres muy flaco"
    | peso / altura^2 <= 25.0 = "Bien, tienes buen peso"
    | peso / altura^2 <= 30.0 = "Vivan los gorditos"
    | otherwise = "Upssss, ganamos la demanda del gym"

-- Funciones por guardas de multiples variables
imc_2 :: (RealFloat variable) => variable -> variable  -> String -> String
imc_2 peso altura nombre
    | peso / altura^2 <= 18.5 = "Eres muy flaco" ++ nombre
    | peso / altura^2 <= 25.0 = "Bien, tienes buen peso" <> nombre
    | peso / altura^2 <= 30.0 = "Vivan los gorditos" <> nombre
    | otherwise = "Upssss, ganamos la demanda del gym" ++ nombre

main :: IO()
main = do
    putStrLn(suerte 7)
    putStrLn(suerte 13)
    putStrLn(suerte 15)

    putStrLn (imc 75 1.91)
    
    putStrLn (imc_2 78 1.91 "Alejandro")