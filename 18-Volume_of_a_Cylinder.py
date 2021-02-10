import math

def volume_of_cylinder(radius, height):
    return height * (math.pi * radius * radius)

print(volume_of_cylinder(int(input("radius: ")), int(input("height:"))))