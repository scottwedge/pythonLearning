#!/usr/bin/env python3

x = 5
y = 5

if x < y:
    z = 100 #lives outside of function too! but only if condition true
    print('x < y: if x is {} and y is {}'.format(x, y))
elif x > y:
    z = 200
    print('x > y: if x is {} and y is {}'.format(x, y))
elif x == y:
    z = 300
    print('x == y: if x is {} and y is {}'.format(x, y))
else: 
    z = 500
    print('something else')  

print('also printing z: {}'.format(z))

# blocks are marked by indentation, & they do not define scope