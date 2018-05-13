-- | Project Euler
-- 1-Find the sum of all the multiples of 3 or 5 below 1000.
-- Optimized
sum [3,6..999] + sum [5,10..999] - sum [15,30..999]
-- Brute force
sum  [x | x <- [0..999], x `mod` 3 == 0 || x `mod` 5 == 0]
