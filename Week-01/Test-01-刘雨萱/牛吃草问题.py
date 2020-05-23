import math

n1 = 10
d1 = 22
n2 = 16
d2 = 10
speed = (n1 * d1 - n2 * d2) / (d1 - d2)
inital = n1 * d1 - speed * d1
n3 = float(input("please input the number of your cows:"))
d3 = inital / (n3 - speed)
print(math.floor((d3)))
