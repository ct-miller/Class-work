
def main():
    another = 'y'
    coffee_file = open('coffee.text', 'a')
    # add records to file
    while another == 'y' or another == 'Y':
        # get the coffee record data.
        print('Enter the following coffee data: ')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        # append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # determine whether the user wants to add another record on file
        print('Do you want to add another record? ')
        another = input('Y = yes, anything else = no: ')

    # close file
    coffee_file.close()
    print('Data appended to coffee.txt.')

main()
