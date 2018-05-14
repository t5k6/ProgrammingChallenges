# Project Euler
# Problem 1 1-Find the sum of all the multiples of 3 or 5 below 1000.
# Optimized
sumby <- function(a) sum(seq(a, 999, by=a))
sumby(3) + sumby(5) - sumby(15)
# 233168
# Brute force
l <- 1:999
sum(l[l %% 3 == 0 | l %% 5 == 0])
# 233168