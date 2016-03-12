'''
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
'''
import math

# Find the upper bound
# math.factorial(9) = 362880
# 9999 < 4*362880 = 1451520
# 99999 < 5*362880 = 1814400
# 999999 < 6*362880 = 2177280
# 9999999 > 7*362880 = 2540160

print(sum([i for i in range(3,100000) if i == sum([math.factorial(int(j)) for j in str(i)])]))