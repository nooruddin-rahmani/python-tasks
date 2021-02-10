seconds = int(input('Enter number of seconds'))
d = seconds // 86400
hr = (seconds % d) // 3600 if d != 0 else seconds // 3600
minutes = (seconds % (d + (hr * 3600))) // 60 if (hr != 0) else seconds // 60
sec = seconds % 60
print(f'{d}:{hr:02d}:{minutes:02d}:{sec:02d}')