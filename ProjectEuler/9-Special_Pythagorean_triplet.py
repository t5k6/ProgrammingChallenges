'''
There exists exactly one Pythagorean triplet (a < b < c) for which a + b + c = 1000
Find a*b*c
'''

for a in range(300):
    for b in range(a,400):
        c = 1000-a-b
        if (a**2+b**2)==c**2:
            print(a,b,c)
            print(a*b*c)

# solution= 200 375 425


