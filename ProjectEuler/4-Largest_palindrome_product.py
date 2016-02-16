'''Find the largest palindrome made from the product of two 3-digit numbers.'''

largest = 0

def palindrome(text):
    for i in range(int(len(text)/2)+1):
        if text[i]!=text[-(i+1)]:
            return False
    return True

for i in range(999,900,-1):
    for j in range(999,900,-1):
        if palindrome(str(i * j)):
            largest = i*j
    if largest >0:
        break

print(largest)






