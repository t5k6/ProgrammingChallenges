with open("Day5-input.txt","r") as f:
    data = f.read()

data = list(data.splitlines())

# Rules for Problem 1:

def nice(data):
    total = 0
    def req1(vowels):
        return len([i for i in vowels if i in 'aeiou'])>= 3

    def req2(twice):
        return sum([twice[i]==twice[i+1] for i in range(len(twice)-1)])>0

    def neg(string):
        return len([i for i in ['ab', 'cd', 'pq', 'xy'] if string.find(i) != -1]) == 0

    for i in data:
        if req1(i) and req2(i) and neg(i): total += 1

    return total

# Rules for Problem 2:

def nice2(data):
    total = 0

    def twice2(string):
        for i,j in enumerate(string):
            pair = string[i:i+2]
            if string[(i+1):].find(pair)>0: return True
        return False

    def neg2(string):
        for i in range(len(string)-2):
            letter = string[i]
            if letter == string[i+2]: return True
        return False

    for i in data:
        if twice2(i) and neg2(i): total += 1

    return total


print("Answer for Problem 1:\t {}".format(nice(data)))
print("Answer for Problem 2:\t {}".format(nice2(data)))





