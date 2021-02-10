v, t = map(float, input('Enter V and T in order:(T <= 10 degrees Celsius, V > 4.8 Km/hr) ').split(' '))

if (v > 4.8) and (t <= 10): 
    print(f'WCI = {round(13.12 + .6215 * t - 11.37 * (v ** .16) + .3965*t*(v**.16))}')
else: 
    print('Could not calculate valid WCI for given values!')