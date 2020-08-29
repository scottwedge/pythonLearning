#!/usr/bin/env python3

x = 2
print('x is {}'.format(x))
print(type(x))

y = 2.1
print('y is {}'.format(y))
print(type(y))

z = 'zzz'
print('z is {}'.format(z))
print(type(z))

a = True
print(f'a is {a}')
print(type(a))

b = None # NoneType
print(f'a is {b}')
print(type(b))


# TUPLE
thing = (1, 2, 3, 4, 5)
print(type(thing))

thing = (1, 'two', 3.0, ['four', 4], 5)
print(type(thing))
print(type(thing[1]))
print(id(thing)) #id will be diff for diff objects but same for same numbers etc


#COMPARE

if x is y:
    print('yes')
else:
    print('nah')

if isinstance(thing, tuple):
    print('yes')
else:
    print('nah')