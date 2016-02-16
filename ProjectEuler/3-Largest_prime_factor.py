'''What is the largest prime factor of the number 600851475143 ?'''


def check_prime(x):
    largest = 0
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0 and is_prime(i) and i > largest:
            largest = i
    print(largest)


def is_prime(x):
    if x < 2: return False
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

check_prime(600851475143)