#!/usr/bin/env python

# Opening display and enter book amount.
print('Welcome to Serendipty Book Store point system!')
purchase_amt = int(input('\n''Enter total number of books purchased for the month: '))

# Display points earned.
if purchase_amt == 0:
    print("You've earned 0 points this month.")
elif purchase_amt == 1:
    print("You've earned 5 points this month.")
elif purchase_amt == 2:
    print("You've earned 15 points this month.")
elif purchase_amt == 3:
    print("You've earned 30 points this month.")
elif purchase_amt >= 4:
    print("You've earned 60 points this month.")
