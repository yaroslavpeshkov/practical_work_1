import math

radius_1 = int(input())
radius_2 = int(input())
if radius_1 <= radius_2:
    print(math.pi*(radius_2 ** 2 - radius_1 ** 2))
else:
    print(math.pi * (radius_1 ** 2 - radius_2 ** 2))
