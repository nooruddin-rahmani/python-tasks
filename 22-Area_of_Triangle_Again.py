# use this formula: sqrt(p(p-a)(p-b)(p-c))
import math

def area_of_triangle(a, b, c):
    p = (a + b + c)/2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))

a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))


print(area_of_triangle(a, b, c))