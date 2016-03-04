'''
Evaluate the sum of all the amicable numbers under 10000.
'''

def amicable(n):
    return sum([i+n/i for i in range(1,int(n**0.5+1)) if n%i==0],-n)

def amicable_total(n):

    return sum([i for i in range(1,n) if i == amicable(amicable(i)) and i != amicable(i)])

print(amicable_total(10000))

# ans = 31626

