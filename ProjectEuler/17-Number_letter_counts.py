'''
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''

words = {1: "one", 2: "two", 3:"three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
         11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
         18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
         70: "seventy", 80: "eighty", 90: "ninety"}

'''
a: 1-99:
b: 100, 200,... : len(1-9)+9*(len("hundred"))
c: 101,102,...  : (b + a)*9
'''


def num_words(num):

    tots = 0

    for i in range(1,num+1):
        if i<20:
            tots += len(words[i])
        elif i<100:
            if i%10==0:
                tots += len(words[i-(i%10)])
            else:
                tots += (len(words[i-(i%10)]) + len(words[i%10]))

    return tots

# Numbers 1-99 repeat 10 times = 8540
x99 = num_words(99)*10
# [1-9]hundred = 99 // one hundred, two hundred, etc.
x100 = num_words(9)+len("hundred")*9
# 101, 102,...,998,999
# [one-nine] +  "hundred and" [one-ninety nine]
# Remaining numbers 99*9=891 = 12474
x101 = num_words(9)*99+len("hundredand")*99*9
x1000 = len("onethousand")

print(x99+x100+x101+x1000)








