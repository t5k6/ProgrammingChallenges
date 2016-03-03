'''
Find the sum of the digits in the number 100!
'''

import math

# a = str(math.factorial(100))
print(sum([int(i) for i in str(math.factorial(100))]))
# answer = 648