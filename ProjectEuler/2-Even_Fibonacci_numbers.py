'''find the sum of the even-valued fibonacci numbers till 4.000.000'''

x = y = 1
sum = 0
while y < 4000000:
    x, y = y, x + y
    if y % 2 == 0:
        sum += y

print(sum)
