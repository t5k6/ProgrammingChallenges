import requests
r = requests.get('https://projecteuler.net/project/resources/p022_names.txt')
names = sorted([name.replace("\"","") for name in r.text.split(",")])

from string import ascii_lowercase as al
letters = {x.upper():i for i, x in enumerate(al, 1)}

total = 0
for idx, name in enumerate(names, 1):
    temp = 0
    for letter in name:
        temp += letters[letter]
    total += (temp * idx)

print(total)