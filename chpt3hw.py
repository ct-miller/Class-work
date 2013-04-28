#!/usr/bin/env python


#HOMEWORK: There are three seating categories at a stadium. For a softball game, Class A seats cost $15, Class B seats cost $12,
# and Class C seats cost $9.
# Write a program that asks how many tickets for each class of seats were sold, and then displays the amount of income generated from ticket sales.


CLASS_A = 15.00
CLASS_B = 12.00
CLASS_C = 9.00

def main():
    #input number of seats sold for each class.
    total_a = float(input('Enter total tickets sold for Class "A": '))
    total_b = float(input('Enter total tickets sold for Class "B": '))
    total_c = float(input('Enter total tickets sold for Class "C": '))
    calc_total_income(total_a, total_b, total_c)

def calc_total_income(a, b, c):
    income_total = a + b + c
    print('This is the total income from ticket sales: $', format(income_total, ',.2f'), sep='')



main()