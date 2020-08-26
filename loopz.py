#!/usr/bin/env python3

# a fibonnaci while-loop:

print('fibonnaci magic!')
a,b = 0,1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print()

# a simple & classy for-loop
words = ['one', 'two', 'three', 'four', 'five']

for i in words:
    print(i)