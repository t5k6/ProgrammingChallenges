'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# Brute force method
normal_sum = sum([i for i in range(101)])**2
square_sum = sum([i**2 for i in range(101)])
print(normal_sum - square_sum)

# Mathematical method
# (a + b + .. + n)^2     = n^2 * (n+1)^2 * 1/4
# (a^2 + b^2 + .. + n^2) = n * (n+1) * (2n+1) * 1/6

