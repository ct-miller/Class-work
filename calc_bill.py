#!/usr/bin/env python

TAX = 0.07
TIP = 0.15

meal_amount = float(input('Enter your meal total here: '))
calc_tax = TAX * meal_amount
calc_tip = TIP * meal_amount
calc_total = calc_tax + calc_tip + meal_amount

print('Here is the tax: ', format(calc_tax, '.2f'))
print('This is the tip amount: ', format(calc_tip, '.2f'))
print('Complete Amount of your meal: ',format(calc_total, '.2f'))