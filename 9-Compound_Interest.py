import math

def solve(p):
    a = 0.04
    return p*(1+a)

SAR = int(input("sarmaya:"))
newSAR = SAR

for i in range(3):
    newSAR = solve(newSAR)
    
    print(f"year: {i+1}: {newSAR:.2f}")