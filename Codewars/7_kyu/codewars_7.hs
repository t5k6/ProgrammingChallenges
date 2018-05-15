-- https://www.codewars.com/kata/complementary-dna/train/haskell
type DNA = [Base]

dnaStrand :: DNA -> DNA
dnaStrand [] = []
dnaStrand (x:xs)
  | x == A = T: dnaStrand xs
  | x == T = A: dnaStrand xs
  | x == G = C: dnaStrand xs
  | x == C = G: dnaStrand xs

-- https://www.codewars.com/kata/exes-and-ohs/train/haskell
import Data.Char
xo :: String -> Bool
xo str = count 'x' (map toLower str) == count 'o' (map toLower str)
count x = length . filter (x==)

-- https://www.codewars.com/kata/get-the-middle-character/train/haskell
getMiddle :: String -> String
getMiddle s
  | odd $ length s = [s !! (div (length s) 2 - mod (div (length s) 2) 1)]
  | even $ length s = [s !! (div (length s) 2 - 1), s !! div (length s) 2]

-- most upvoted 
getMiddle' "" = ""
getMiddle' [a] = [a]
getMiddle' [a,b] = [a,b]
getMiddle' (_:x) = getMiddle (init x)

-- https://www.codewars.com/kata/make-a-function-that-does-arithmetic/haskell
data Operation = Add | Divide | Multiply | Subtract deriving (Eq, Show, Enum, Bounded)

arithmetic :: Fractional a => a -> a -> Operation -> a
arithmetic a b operator
  | operator == Add = (+) a b
  | operator == Subtract = a-b
  | operator == Divide = a/b
  | operator == Multiply = a*b

-- https://www.codewars.com/kata/relatively-prime-numbers/train/haskell/5a894d99b17101d773000047
relativelyPrime :: Integral t => t -> [t] -> [t]
relativelyPrime n l = [ x | x <- l, gcd n x == 1]

-- https://www.codewars.com/kata/vowel-count/train/haskell
getCount [] = 0
getCount (x:xs)
  | x `elem` "aeiou" = 1 + getCount xs
  | otherwise = getCount xs