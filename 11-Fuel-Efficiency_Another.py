# 1 mile = 1609 miter
# 1 gallon = 3.78541 liter

# the question is: 
#   x mile      ? liter
#  -------- =? ---------
#   gallon       100km


def ustoother(us):
    # change mile to miter
    x = us * 1609
    # we need 1 gallon for 'x' miters.

    y = 100 * 1000 / x
    


    # change gallon to liter and multiply with 'y'
    z = y * 1 * 3.78541
    
    # 'z' liter is needed for 100km 
    return z

print(ustoother(int(input("Enter Miles-per-Gallon: (returns: liters / 100km)"))))
