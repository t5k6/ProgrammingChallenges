'''
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
'''


with open("Day2-input.txt","r") as f:
    data = f.read()

tot_surface_area = 0
ribbon_length = 0

data = list(data.splitlines())

for line in data:
    temp =[int(n) for n in line.split("x")]
    tot_surface_area += 2*temp[0]*temp[1]+2*temp[0]*temp[2]+2*temp[1]*temp[2]+min(temp[0],temp[1],temp[2])
    ribbon_length += 2*(min(temp[0], temp[1]) + min(temp[1],temp[2])) + (temp[0]*temp[1]*temp[2])

print(tot_surface_area)
print(ribbon_length)



