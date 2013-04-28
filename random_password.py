#!/usr/bin/env python

from random import randint
import string

charset = string.ascii_letters + string.digits + '!@#$&*()[]'
print (''.join([charset[randint(0, len(charset)-1)] for i in range(16)]))