# Write a program that reads the random numbers file you generated in lab 7,
# display the numbers, and then display the following data:
# • The total of the numbers
# • The number of random numbers read from the file

# set accumulator and count variables to zero.
total = 0
count = 0

# open the number file.
numb = open('number_file.txt', 'r')

# set a for loop to read each number in the file
for line in numb:
    # add one to the count variable
    count += 1

    # turn each line into a int from a string
    amount = int(line)

    # get the total of the numbers
    total += amount

    # print each number
    print(amount)

# close the file.
numb.close()

print('There are', count, 'numbers in this file with a total of', total)
