'''
Find the sum of all the primes below two million.
'''

def rwh_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::i]=[False]*((n-i*i-1)//i+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

print(sum(rwh_primes(2000000)))

