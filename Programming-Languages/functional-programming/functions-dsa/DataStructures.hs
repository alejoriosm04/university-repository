import Data.List

main :: IO ()
main = do
    -- Declare a list of numbers
    putStrLn "Declare a list of numbers"
    let listNumbers = [1, 3, 5, 7]
    print listNumbers
    -- Declare a tuple of numbers
    putStrLn "Declare a tuple of numbers"
    let tupleNumbers = (2, 4, 6, 8)
    print tupleNumbers

    -- Concatenate two lists
    putStrLn "Concatenate two lists"
    let numbers1 = [1,2,3,4]
    let numbers2 = [5,6,7,8]
    print (numbers1 ++ numbers2)

    -- Concatenate strings with :
    putStrLn "Concatenate strings with :"
    let word = "n Gato"
    print ('U' : word)

    -- Create lists with ranges
    putStrLn "Create lists with ranges"
    let evenNumbers = [2, 4..10]
    print evenNumbers

    -- Functions Data.List
    putStrLn "Functions Data.List"
    -- Intersperse
    putStrLn "Intersperse"
    let lista = [1..5]
    print (intersperse 0 lista)
    let name = "Alejandro"
    print (intersperse '-' name)

    -- Intercalate
    putStrLn "Intercalate"
    let lista = [0,0,0]
    let lista2 = [[1,2,3],[4,5,6],[7,8,9]]
    print (intercalate lista lista2)

    -- Transpose
    putStrLn "Transpose"
    let matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print (transpose matrix)
    -- Sum of polynomials
    putStrLn "Sum of polynomials"
    let pol1 = [0,3,5,9]
    let pol2 = [10,0,0,9]
    let pol3 = [8,5,1,-1]
    let matrix = [pol1, pol2, pol3]
    print (map sum $ transpose matrix)