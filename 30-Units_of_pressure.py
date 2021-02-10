p = float(input('Enter pressure in kilopascals: '))
pound = p * .145038
merc = p * 7.501875
atm = p * .09869

print(f"""
{p} kilopascals = {pound} pound per square inch
{p} kilopascals = {merc} millimeters of mercury
{p} kilopascals = {atm} atm
""")