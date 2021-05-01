# Using with as context manager

with open('file.txt', 'w') as file:
    file.write('hello again 1!')


# Without using with

file = open('file.txt', 'w')
try:
    file.write('hello, world finally!')
finally:
    file.close()