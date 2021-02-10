import math as mt

n, s = map(int, input('Enter values of n and s: ').split(' '));
p = s * n
a = s / (mt.tan(mt.pi / n) * 2)
print(f'Area of polygon is {(p * a) / 2: .2f6 }')