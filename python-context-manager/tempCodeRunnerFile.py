file = open('file.txt', 'w')
try:
    file.write('hello, world finally!')
finally:
    file.close()