

#open file named numbers.txt
integers = open('numbers.txt', 'w')

# for loop to add numbers 1 to 10 to file
for count in range(1,11):
    integers.write(str(count) + '\n')

# Display message that numbers are added to file
print('Numbers one through ten have been saved to the numbers.txt file.')

# close file
integers.close()



