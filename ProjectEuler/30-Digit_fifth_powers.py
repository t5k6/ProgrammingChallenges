'''
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

# Step 1 - Find the upper limit
# 9^5 = 59049
# 59049*6 = 354294
# 59049*7 = 413343
# There is no point trying numbers bigger than 6 digit (354294)

# Step 2 - Brute force all numbers smaller than 354294

print(sum([i for i in range(1000,354294) if i == sum([pow(int(num),5) for num in str(i)])]))

# ans = 443839