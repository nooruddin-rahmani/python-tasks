days, hours, minutes, seconds = map(float, input('Enter number of days, hours, minutes, and seconds in order space seperated: ').split(' '))
total_sec = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds
print('Number of total seconds: ', total_sec)