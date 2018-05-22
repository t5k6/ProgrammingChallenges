'''
What is the 10001st prime number?
'''

def is_prime(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

i = 2
n = 0

while n != 10001:
    if is_prime(i):
        n += 1
    i += 1

print(i-1)  # 104743