--
-- What is the 10001st prime number?
--

isPrime n (x:xs) = (x*x > n) || (mod n x /= 0) && (isPrime n xs)
(2 : filter (\x -> isPrime x primes) [3,5..]) !! 10000