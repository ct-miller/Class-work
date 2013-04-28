#!/usr/bin/env python

import sys
import datetime


day = int(input('Enter two digit day: '))
month = int(input('Enter two digit month: '))
year = int(input('Enter two digit year: '))


user_date = "%d/%d/%d" % (day, month, year)

try:
    user_date = datetime.datetime.strptime(user_date, "%m/%d/%y")
except ValueError:
    print("Invalid date asshole")
    sys.exit(1)




date = month * day

if date == year:
    print('\n''This date is magic!')
else:
    print('\n''This date is not magic.')

#run(host='localhost', port=8080, debug=True)