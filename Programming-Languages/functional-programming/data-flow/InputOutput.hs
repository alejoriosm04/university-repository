main :: IO ()
main = do
    -- Example of user-input with getLine
    putStrLn "Example of user-input with getLine"
    putStrLn "What's your first name?"
    firstName <- getLine
    putStrLn "What's your last name?"
    lastName <- getLine
    putStrLn $ "Hi " ++ firstName ++ " " ++ lastName ++ ", how are you?"

    -- Example of output with putStr and putStrLn
    putStrLn "Example of output with putStr and putStrLn"
    putStr "Hey, "
    putStr "I'm "
    putStrLn "Alex!"

    -- Example of output with print
    putStrLn "Example of output with print"
    print True
    print 2
    print "haha"
    print 3.2
    print [3,4,3]