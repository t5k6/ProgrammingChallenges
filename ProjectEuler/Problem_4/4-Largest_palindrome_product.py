'''Find the largest palindrome made from the product of two 3-digit numbers.'''

largest = 0

def palindrome(text):
    return text == text[::-1]

for i in range(999,900,-1):
    for j in range(999,900,-1):
        if (i*j)%11==0 and palindrome(str(i * j)) and (i*j) > largest:
            largest = i*j

print(largest) # 906609