'''
n → n/2 (n is even)
n → 3n + 1 (n is odd)
'''


def collatz(x):
    ll = []
    ll.append(x)
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        elif x % 2 == 1:
            x = 3 * x + 1
        ll.append(x)
    ll.append(1)
    return ll


greatest = 0
num = 0
for i in range(1000000, 800000, -1):
    temp = len(collatz(i))
    if temp > greatest:
        greatest = temp
        num = i

print(num)
