# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

x = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2  # 9699690

found: bool = False
while not found:
    for i in range(1, 21):
        if x % i:
            break
    else:
        print(f"Answer is :{x}")  # 232792560
        found = True
    x += 9699690
