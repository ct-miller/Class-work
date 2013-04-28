#!/usr/bin/env python

#Assign size to base.
base = 8

# Make inverted astrix triangle.
for r in range(base):
    print('*'*base, end='\n')
    base -= 1
