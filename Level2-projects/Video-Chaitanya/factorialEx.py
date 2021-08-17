import math
import aolme2

for n in range(1,21):
    print(n, "! =", math.factorial(n))
    print("Number of tours for n=", n, " points ", 20)

num_of_cities = 3
show_tours(num_of_cities)