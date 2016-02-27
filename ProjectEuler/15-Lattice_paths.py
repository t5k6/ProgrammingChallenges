'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
Shortest path requires 40 steps; 20 to the right and 20 to the down. So C(40/20)
'''

# C( 40! / (20! * (40-20)!) )

import math
print(math.factorial(40)/(math.factorial(20)*math.factorial(40-20)))

# ans = 137846528820