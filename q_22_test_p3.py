
# Open numbers file
integers = open('numbers.txt','a')

# for loop to add numbers 11 to 21 in file.
for i in range(11,21):
    integers.write(str(i) + '\n')

# Statement, numbers are added to file.
print('Integers 11 through 20 saved to the numbers file.')

# close file
integers.close()
