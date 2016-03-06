'''
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import itertools

for idx,val in enumerate(itertools.permutations([i for i in range(10)],10),1):
    if idx == 1000000:
        print(''.join([str(i) for i in val]))
        break

# ans = 2783915460