--Find the largest palindrome made from the product of two 3-digit numbers.

maximum [x*y | x <- [900..999], y <- [900..999], reverse (show (x * y)) == show (x * y)] -- 906609