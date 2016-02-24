'''
What is the value of the first triangle number to have over five hundred divisors?
'''


def triangle_divisors(x):
    def triangle(y):
        tot = 0
        for i in range(1, y + 1):
            tot += i
        return tot

    def factors(n):
        factor_list = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factor_list.extend((i, n // i))
        return factor_list

    temp = x
    cont = True
    while cont:

        tria = triangle(temp)
        divs = factors(tria)

        if len(divs) > x:
            # print("Tria = {}, Len = {}, Div = {}".format(tria,len(divs), divs))
            cont = False

        temp += 1
    print(tria)


print(triangle_divisors(500))

# 100-73920
# 500-76576500
