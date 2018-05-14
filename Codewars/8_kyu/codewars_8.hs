-- https://www.codewars.com/kata/century-from-year/train/haskell/5ad8c29e32d79e80090000a7
century::Int -> Int
century year
  | mod year 100 == 0 = div year 100
  | otherwise         = div year 100 + 1

-- https://www.codewars.com/kata/dna-to-rna-conversion/train/haskell/5a7efcb3fd57775b3a0000a4
dnaToRna :: String -> String 
dnaToRna [] = []
dnaToRna (x:xs)
  | [x] == ['T'] = ['U'] ++ dnaToRna xs
  | otherwise = [x] ++ dnaToRna xs

-- https://www.codewars.com/kata/is-the-string-uppercase/train/haskell/5a8b10e9fd8c0691230000d4
import Data.Char (isLower)

isUpperCase :: String -> Bool
isUpperCase = not . any isLower

isUpperCase' :: String -> Bool
isUpperCase' xs = length [x|x<-xs, x `elem` ['a'..'z'] ++ ['A'..'Z']] == length [x|x<-xs, x `elem` ['A'..'Z']]

-- https://www.codewars.com/kata/reversed-strings/train/haskell/5a48e6a6880385b54e000034
solution :: String -> String
solution word = reverse word

-- https://www.codewars.com/kata/they-say-that-only-the-name-is-long-enough-to-attract-attention-they-also-said-that-only-a-simple-kata-will-have-someone-to-solve-it-this-is-a-sadly-story-number-1-are-they-opposite/train/haskell
import Data.Char
isOpposite :: String -> String -> Bool
isOpposite [] _ = False
isOpposite _ [] = False
isOpposite (x:xs) (y:ys)
  | length xs /= length ys = False
  | isUpper x = (toLower x == y) && isLower y
  | isLower x = (toUpper x == y) && isUpper y
  | otherwise = isOpposite xs ys

