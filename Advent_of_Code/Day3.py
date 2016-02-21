'''
Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
'''

with open("Day3-input.txt","r") as f:
    data = f.read()



# [x, y]
places = {(0,0): 0}

x = 0
y = 0
for move in data:

    if move == '^':
        y += 1
    elif move == "v":
        y -= 1
    elif move == ">":
        x += 1
    elif move == "<":
        x -= 1
    if (x, y) not in places.keys():
        places[(x, y)] = 1
    else:
        places[(x, y)] += 1

print("Problem 1 solution: {}".format(len(places.keys())))

# Problem 1 solution : 2592

ttt = iter(data)

s1 = []
s2 = []
for move1, move2 in zip(ttt, ttt):
    s1.append(move1)
    s2.append(move2)

# for move in data[1::2]:
#     s2.append(move)


places_s1 = {(0,0): 0}

x = 0
y = 0

for move in s1:

    if move == '^':
        y += 1
    elif move == "v":
        y -= 1
    elif move == ">":
        x += 1
    elif move == "<":
        x -= 1
    if (x, y) not in places_s1.keys():
        places_s1[(x, y)] = 1
    else:
        places_s1[(x, y)] += 1

x = 0
y = 0

for move in s2:

    if move == '^':
        y += 1
    elif move == "v":
        y -= 1
    elif move == ">":
        x += 1
    elif move == "<":
        x -= 1
    if (x, y) not in places_s1.keys():
        places_s1[(x, y)] = 1
    else:
        places_s1[(x, y)] += 1


print("Problem 2 solution: {}".format(len(places_s1.keys())))


