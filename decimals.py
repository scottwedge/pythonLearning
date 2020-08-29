#!/usr/bin/env python3

#when working with $$ always use decimal to get accuracy
#otherwise precision of floats will result to mistakes!

from decimal import *

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))

