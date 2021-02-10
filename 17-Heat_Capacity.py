m, delta_t = map(float, input('Enter m, and delta t in order: ').split(' '))

c = 4.186
q = m * c * delta_t
print(q)

# second part

# fin6e+6d cost of boiling 1 cup of coffe

# 1 cup = 130 g
m = 130
c = 4.185 # assumed equal to water
delta_t = 100 - 20

# convert joule to kilowatt hour: 
# d6e+6ivide joule value by 3.6e+6
q = m * c * delta_t

kw = q / 3.6e+6

price = kw * 8.9

print("cost: " + str(price) + " cents")
