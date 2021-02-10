width_in_feet = float(input("Enter the Width of field in feet: "))
lenght_in_feet = float(input("Enter the Lenght of field in feet: "))
area_in_feet = width_in_feet * lenght_in_feet
#1ft**2 = 0.09m**2
#1ft**2 = 2.22*10**(-5)acres
area_in_acres = area_in_feet * ((22.22)*(10**(-5)))
print("Area in Acres : ", area_in_acres)

