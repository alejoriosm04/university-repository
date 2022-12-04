import Data.List
import System.IO

-- Int: -2^63 to 2^63
minInt = minBound :: Int
maxInt = maxBound :: Int

-- Integer: no range

-- Double: up to 11 points of precision

-- Bool: True False

-- Char: single unicde character defined with ''

-- Tuple: lists with 2 values

-- Permanent value declaration
always5 :: Int
always5 = 5 -- value will never change

-- Sum all numbers 1 to 1000
sumOfNums = sum [1..1000]

-- Basic math operations
addEx = 5 + 4
subEx = 5 - 4
multEx = 5 * 4
divEx = 5 / 4
modEx = mod 5 4
modEx2 = 5 `mod` 4

-- use parantheses when dealing with negative numbers
negNumEx = 5 + (-4)

-- sqrt works with floats, so we have to convert our int using 'fromIntegral'
num9 = 9 :: Int
sqrtOf9 = sqrt (fromIntegral num9)

-- MATH FUNCTIONS
piVal = pi
ePow9 = exp 9
logOf9 = log 9
squared9 = 9 ** 2
truncateVal = truncate 9.999
roundVal = round 9.999
ceilingVal = ceiling 9.999
floorVal = floor 9.999
-- Also sin, cos, tan, asin, atan, acos, sinh, tanh, cosh,
-- asinh, atanh, and acosh

-- Logic operators in variables
trueAndFalse = True && False
trueOrFalse = True || False
notTrue = not(True)

-- LISTS
-- can only add to front of lists
primeNumbers = [3,5,7,11]
morePrimes = primeNumbers ++ [13,17,19,23,29]
primeAndSome = morePrimes ++ [30..1000]
favNums = 2 : 7 : 21 : 66 :[] -- combine numbers in to a list
multiList = [[3,5,7],[11,13,17]]
morePrimes2 = 2 : morePrimes
lenPrime = length morePrimes2 -- return length
revPrime = reverse morePrimes2 -- reverse list
isListEmpty = null morePrimes2 -- return whether empty or not
secondPrime = morePrimes2 !! 1 -- return second index of list (lists are base 0)
firstPrime = head morePrimes2 -- first value in list
lastPrime = last morePrimes2 -- last value
primeInit = init morePrimes2 -- return everything except last value
first3Primes = take 3 morePrimes2 -- take first 3 values
removedPrimes = drop 3 morePrimes2 -- remove first 3 values
is7InList = 7 `elem` morePrimes2 -- check for 7 in List
is7InList2 = elem 7 morePrimes2 -- same thing as above
maxPrime = maximum morePrimes2
minPrime = minimum morePrimes2

newList = [2,3,5]
prodPrimes = product newList -- product of values in List

zeroToTen = [0..10] -- list from 0 to 10
evenList = [2,4..20] -- all even numbers using first 2 numbers to define rule
oddList = [1,3..20]
letterList = ['A', 'C' .. 'Z']
infinPow10 = [10,20..]

many2s = take 10 (repeat 2) -- generate ten 2s
many3s = replicate 10 3 -- same thing
many4s = 10 `replicate` 4 -- same thing
cycleList = take 10 (cycle [1,2,3,4,5]) -- repeat defined list

-- defines a list and mulitplies every number by 2, then adds it to 'listTimes2'
listTimes2 = [x * 2 | x <- [1..10]]

-- defines a list and mulitplies every number by 3, then adds it to 'listTimes3'
-- then only returns values that are less than or equal to 50
listTimes3 = [x * 3 | x <- [1..20], x * 3 <= 50]

-- defines a list and adds numbers only divisible by 13 and 9 to 'divisBy9N13'
divisBy9N13 = [x | x <- [1..500], x `mod` 13 == 0, x `mod` 9 == 0]

sortedList = sort [9,1,8,3,4,7,6] -- sorts list low to high

-- adds each value of first list to the value of the second and returns the
-- results as a list
sumOfLists = zipWith (+) [1..5] [6..10]

-- filter through list for values greater than 5
listBiggerThan5 = filter (>5) morePrimes

-- take all even numbers up to 20
evensUpTo20 = takeWhile (<= 20) [2,4..]

-- multiplies numbers in list from left to right
multOfList = foldl (*) 1 [2..5]

--multiples numbers in list from right to left
multOfListR = foldr (*) 1 [2..5]

-- Define a list and set each number to the power of 3 and add it to 'pow3List'
pow3List = [3^n | n <- [1..10]]

-- '[x * y | y <- [1..10]]' is the operation to perform on a defined list
multTable = [[x * y | y <- [1..10]] | x <- [1..10]]
--
-- ==============[END OF LISTS]============= --
--

-- Tuples
randTuple = (1, "Random Tuple")
bobSmith = ("Bob Smith", 52)
bobsName = fst bobSmith -- returns first value in tuple
bobsAge = snd bobSmith -- returns second value in tuple

names = ["Bob", "Mary", "Tom"]
addresses = ["123 Main", "234 North", "567 South"]

-- creates tuple pairs by combining names & addresses
namesAndAddresses = zip names addresses

-- Functions
{-
main = do
  putStrLn "What's your name"
  name <- getLine
  putStrLn ("Hello " ++ name)
-}

-- Type Declaration for function:
addMe :: Int -> Int -> Int
-- funcName param1 param2 = operations (returned value)
addMe x y = x + y

-- No type declaration
sumMe x y = x + y

-- Add tuples with ints inside and return a tuple with ints inside
addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuples (x, y) (x2, y2) = (x + x2, y + y2)

whatAge :: Int -> String
whatAge 16 = "You can drive"
whatAge 18 = "You can vote"
whatAge 21 = "You're an adult"
whatAge _ = "Nothing important"

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

prodFact n = product [1..n] -- easier way of doing factorials


-- Guards
isOdd :: Int -> Bool
isOdd n
  | n `mod` 2 == 0 = False
  | otherwise      = True

whatGrade :: Int -> String
whatGrade age
  | (age >= 5) && (age <= 6) = "Kindergarten"
  | (age > 6) && (age <= 10) = "Elementary"
  | (age >10) && (age <= 14) = "Middleschool"
  | (age > 14) && (age <= 18) = "Highschool"
  | otherwise = "Go to college"

batAvgRating :: Double -> Double -> String
batAvgRating hits atBats
  | avg <= 0.200 = "Terrible Batting Average"
  | avg <= 0.250 = "Average Player"
  | avg <= 0.280 = "Solid m8"
  | otherwise = "It's lit"
  where avg = hits / atBats

getListItems :: [Int] -> String
getListItems [] = "Your list is empty"
-- return first value in list
getListItems (x:[]) = "Your lists starts with " ++ show x
-- return first and second value in list
getListItems (x:y:[]) = "Your list contains " ++ show x ++ " and " ++ show y
-- return first value and then the rest
getListItems (x:xs) = "The 1st item is " ++ show x ++ " and the rest are " ++ show xs

getFirstItem :: String -> String
getFirstItem  [] = "Empty String"
-- return the first value in the string
getFirstItem all@(x:xs) = "The first letter in " ++ all ++ " is " ++ [x]

-- Higher order functions
times4 :: Int -> Int
times4 x = x * 4
-- apply function to list using 'map'
listTimes4 = map times4[1..5]

multBy4 :: [Int] -> [Int]
multBy4 [] = []
multBy4 (x:xs) = times4 x : multBy4 xs

-- explanation of above code --
-- [1,2,3,4] : x = 1 | xs = 2,3,4
-- [2,3,4] : x = 2 | xs = 3,4
-- etc..

areStringsEq :: [Char] -> [Char] -> Bool
areStringsEq [] [] = True
areStringsEq (x:xs) (y:ys) = x == y && areStringsEq xs ys
areStringsEq _ _ = False

doMult :: (Int -> Int) -> Int
doMult func = func 3 -- func is variable name for input function
                     -- in this case, 'times4'
                     -- 'times4' = (Int -> Int) so passing it as func is legal
num3Times4 = doMult times4

getAddFunc :: Int -> (Int -> Int)
getAddFunc x y = x + y
adds3 = getAddFunc 3
fourPlus3 = adds3 4

-- Lambdas --
dbl1to10 = map (\x -> x * 2) [1..10]

-- Conditionals --
-- < > <= >= == /=
-- || &&

-- If statement. Must use else
doubleEvenNumber y =
  if (y `mod` 2 /= 0)
    then y
    else y * 2

-- Case statement
getClass :: Int -> String
getClass n = case n of
  5 -> "Go to kindergarten"
  6 -> "Go to elementary school"
  _ -> "Go home"

-- Enumerables
data BaseballPlayer = Pitcher
                    | Catcher
                    | Infielder
                    | Outfield
                    deriving Show
barryBonds :: BaseballPlayer -> Bool
barryBonds Outfield = True
barryInOF = print(barryBonds Outfield)

-- Enumerabels without static definitions
-- Define type instead and allow dynamic definitions
data Customer = Customer String String Double
  deriving Show
tomSmith :: Customer
tomSmith = Customer "Tom Smith" "123 Main" 20.50
getBalance :: Customer -> Double
getBalance (Customer _ _ b) = b

data RPS = Rock | Paper | Scissors
shoot :: RPS -> RPS -> String
shoot Paper Rock = "Paper Beats Rock"
shoot Rock Scissors = "Rock Beats Scissors"
shoot Scissors Paper = "Scissors Beats Paper"
shoot Scissors Rock = "Scissors Loses to Rock"
shoot Paper Scissors = "Paper Loses to Scissors"
shoot Rock Paper = "Rock Loses to Paper"
shoot _ _ = "Error"

-- $ is used to remove parantheses
data Shape = Circle Float Float Float | Rectangle Float Float Float Float
  deriving Show
area :: Shape -> Float
area (Circle _ _ r) = pi * r ^ 2
area (Rectangle x y x2 y2) = (abs $ x2 -x) * (abs $ y2 - y)

sumValue = putStrLn (show (1 + 2))
-- Does the same thing as above but looks cleaner
sumValue2 = putStrLn . show $ 1 + 2

areaOfCircle = area (Circle 50 60 20)
areaOfRect = area $ Rectangle 10 10 100 100

-- Type Classes --
data Employee = Employee { name :: String,
                          position :: String,
                          idNum :: Int
                          } deriving (Eq, Show)
samSmith = Employee {name = "Sam Smith", position = "Manager", idNum = 1000}
isSamSam = samSmith == samSmith
samSmithData = show samSmith

data ShirtSize = S | M | L
instance Eq ShirtSize where
  S == S = True
  M == M = True
  L == L = True
  _ == _ = False

instance Show ShirtSize where
  show S = "Small"
  show M = "Medium"
  show L = "Large"

smallAvail = S `elem` [S, M, L]
theSize = show S

-- Define Custom Type Classes --
class MyEq a where
  areEqual :: a -> a -> Bool

instance MyEq ShirtSize where
  areEqual S S = True
  areEqual M M = True
  areEqual L L = True
  areEqual _ _ = False

newSize = areEqual M M

-- I/O --
sayHello = do
  putStrLn "What's your name"
  name <- getLine
  putStrLn $ "Hello " ++ name

writeToFile = do
  theFile <- openFile "text.txt" WriteMode
  hPutStrLn theFile ("Random line of text\nJake is cool")
  hClose theFile

readFromFile = do
  theFile2 <- openFile "text.txt" ReadMode
  contents <- hGetContents theFile2
  putStr contents
  hClose theFile2

-- Fibonacci Sequence --
fib = 1 : 1 : [a + b | (a, b) <- zip fib (tail fib)]
fibOut = take 20 fib -- first 20 number of the fib seq