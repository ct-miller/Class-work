
#Set accumulator variable.
total = 0.0

#Open numbers file
integers = open('numbers.txt', 'r')

#Statement before displaying file contents
print('This is the content in the number file: ')

# for loop to display file contents
for line in integers:
    amount = float(line)
    line = line.rstrip('\n')
    print(line)
    total += amount

#close file
integers.close()
#Display total
print('This is the total: ', total)

