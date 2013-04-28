#!/usr/bin/env python

# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the month,
# and keep a running total. When the loop finishes,
# the program should display the amount that the user is over or under budget.

budget = float(input('Enter total monthly budget: '))
total = 0.0

print('\nEnter your expenses. When done, type done.')
while True:
    expense = input('Enter amount for one of your expenses or done if you\'re finished: ')
    if expense == 'done':
        break
    else:
       total += float(expense)

if total > budget:
    under_over = 'over'
    difference = total - budget
else:
    under_over = 'under'
    difference = budget - total

print('\nYour total is %.2f and you are %s budget by %.2f' % (total, under_over, difference))