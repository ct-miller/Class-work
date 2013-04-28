# Get budget amount.
budget = float(input('Enter your monthly budget: '))

# set accumulator variable.
total = 0.0
# Set expense variable to 1 so that it can true in the while loop.
expense = 1

# Instructions.
print('Enter each expense and press enter. Enter "0" when complete.')

# while loop to get all the expenses.
while expense != 0:
    expense = float(input('Enter amount of expense: '))
    if expense == 0: break
    total += expense

# Display total.
print ('Here is the total: $', format(total, '.2f'), sep='')

# Display if over budget or under.
if total > budget:
    over = total - budget
    print("You're over budget by",format(over, '.2f'))

elif total < budget:
    under = budget - total
    print ("You're under budget by", format(under, '.2f'))


