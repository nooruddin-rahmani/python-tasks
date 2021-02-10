
def calculateHeight(foot, inch):
    return 30.48 * foot + 2.54 * inch

foot = float(input("foot: "))
inch = float(input("inch: "))

print(calculateHeight(foot, inch))