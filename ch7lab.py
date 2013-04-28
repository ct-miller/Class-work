#   Write a program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 100.
# The application should let the user specify how
# many random numbers the file will hold.

import sys
import random

#generate random number
def generate_random_number(max=100):
    return random.randint(1, max)

# get the amount of numbers to be stored in the file
amt = int(input('Enter the amount of random numbers to be stored: '))

#open file
number_file = open('number_file.txt', 'w')

# write numbers to file.
for i in range(amt):
    number_file.write(str(generate_random_number()) + '\n')

#close number file.
number_file.close()

#give client notice the numbers have been saved.
print('Numbers have been store in number_file.txt')

