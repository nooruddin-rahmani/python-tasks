import math as mt
t1, g1 = map(
    mt.radians, map(float, input('Enter coordinates of first position: ').split(' '))
    )
t2, g2 = map(
    mt.radians, map(float, input('Enter coordinates of second position: ').split(' '))
)
acos_args = mt.sin(t1) * mt.sin(t2) + mt.cos(t1) * mt.cos(t2) * mt.cos(g1 - g2)
print(6371.01 * mt.acos(acos_args))