import math

raios = [3.4, 1.2, 11.3, 2.5, 5]

areas = list(map(lambda r: math.pi * (r ** 2), raios))

print(areas)