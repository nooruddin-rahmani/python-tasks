# PV = nRT
#
# R= 8.31446261815324 * 10^3

# p: pressure in Pascal
# v: volume in liter
# t: temperature in kalvin
# returns: n in mole.

def ideal_gas(p, v, t):
    return (p * v) / (8.31446261815324 * 1000 * t)


p = float(input("P: "))
v = float(input("V: "))
t = float(input("T: "))

print(ideal_gas(p, v, t))

