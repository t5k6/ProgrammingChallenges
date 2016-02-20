with open("Day1-input.txt","r") as f:
    data = f.read()
'''
"(" means go up one floor, and ")" means go down one floor.
'''

# Problem 1: find the floor
# Problem 2: Find the character where Santa goes to basement for the first time

stairs = 0
char_total = 0
first_base = 0

for stair in data:
    char_total += 1
    if stair == "(":
        stairs += 1
    elif stair == ")":
        stairs -= 1
    if stairs == -1:
        first_base = char_total


print("Floor Santa is on: {}".format(stairs))
print("First basement character: {}".format(first_base))