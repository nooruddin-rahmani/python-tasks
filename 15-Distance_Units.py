
def solve(feet):

    # 1 foot = 12 inch
    inch = feet * 12

    # 1 mile = 5280 feet
    mile = feet / 5280
    
    # 1 mile = 3 yard
    yard = mile * 3

    print(inch)
    print(mile)
    print(yard)

solve(int(input("Enter foot to convert to inch, yard and mile: ")))