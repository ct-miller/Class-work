

# Entering charge account numbers in a list.
charge_nums = ['5658845','4520125','7895122',
               '8777541','8451277','1302850',
               '8080152','4562555','5552012',
               '5050552','7825877','1250255',
               '1005231','6545231','3852085',
               '7576651','7881200','4581002']

# open and close charge_accounts.txt file to write and assign it to accounts variable.
with open('charge_accounts.txt', 'w') as accounts:
    #for loop to add charge_nums list into file.
    for acct in charge_nums:
        accounts.write("{}\n".format(acct))

#open and close charge_accounts.txt file to read
with open('charge_accounts.txt', 'r') as accounts:
    #for loop to read the lines in accounts.
    for num in accounts:
        accounts = accounts.read()

# test the while loop
search = input('Enter a charge account number or -1 to stop: ')
while search != '-1':
    if search in accounts:
        print('Charge account number is valid!', '\n')
        search = input('Enter a charge account number or -1 to stop: ')
    else:
        print('Charge account not found', '\n')
        search = input('Enter another charge account number: ')

