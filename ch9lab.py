# ask input from the user. Enter several digits
digit = input('Enter several single-digit numbers, no punctuation needed: ')
# Space
print()

# open a list to add numbers to.
add = []

# for loop to get individual numbers from 'digit' and append to list.
for n in digit:
    add.append(n)
    # change the string numbers into int numbers.
    add = [int(n) for n in add]

# find the total and print!
total = sum(add)
print('This is the total of your numbers: ',total)