
import math

def area(r):
    return math.pi * r * r

def volume(r):
    return (4 / 3) * math.pi * r * r * r

r = int(input("Enter Radius: "))
print(area(r))
print(volume(r))