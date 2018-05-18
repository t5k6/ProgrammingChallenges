-- Find the difference between the sum of the squares of the first one hundred natural 
-- numbers and the square of the sum.
-- with list comprehensions
sumOfSquares = ...
squaresOfsum = sum [1..100] * sum [1..100]
answer = squaresOfsum - sumOfsquares

-- # Mathematical method
-- # (a + b + .. + n)^2     = n^2 * (n+1)^2 * 1/4
-- # (a^2 + b^2 + .. + n^2) = n * (n+1) * (2n+1) * 1/6

sumOfSquares' = sum . map (^ 2)
squareOfSums' = (^ 2) . sum
diff ls       = squareOfSums' ls - sumOfSquares' ls
diff [1..100]