
import os

delete_numbers = ('16', '17', '18')

integers = open('numbers.txt', 'r')
temp_file = open('temp.txt', 'a')


for line in integers:
    line = line.strip('\n')
    if line not in delete_numbers:
        temp_file.write(str(line) + '\n')
    else:
        print("Removing {}".format(line))


integers.close()
temp_file.close()

os.remove('numbers.txt')
os.rename('temp.txt', 'numbers.txt')



#with open('numbers.txt', 'r') as number_file:
#    cleaned_numbers = [n for n in number_file.readlines() if n.strip() not in delete_numbers]
#
#with open('numbers.txt', 'w') as number_file:
#    for num in cleaned_numbers:
#        number_file.write(num)
