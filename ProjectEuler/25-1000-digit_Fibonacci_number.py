'''
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

x = y = 1
ind = 2
while True:
    x, y = y, x + y
    if len(str(x))==1000:
        print("Index of F: {0}".format(ind))
        break
    ind += 1



