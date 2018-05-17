-- Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

foldl (lcm) 1 [1..20] --232792560