-- | Project Euler
-- 2-
let calc = sum . filter even . takeWhile (<=4000000) $ fibs
             where fibs =  1:1:zipWith (+) fibs (tail fibs)