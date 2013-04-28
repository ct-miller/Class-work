import os

integers = open('numbers.txt', 'r')
new = open('temp.txt', 'w')

modify = ('10')

for line in integers:
    if line == '10':
        new.write('50')
    else:
        new.write(line + '\n')

integers.close()
new.close()

os.remove('numbers.txt')
os.rename('temp.txt', 'numbers.txt')

