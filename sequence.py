#!/usr/bin/env python3

x = {1, 2, 3, 4, 5}
for i in x:
    print('i is {}'.format(i))

y = range(10)  #range is immutable
for i in y:
    print('i is {}'.format(i))

xy = list(range(10)) #must convert to list to mutate
xy[2] = 100
for i in xy:
    print('i is {}'.format(i))

z = range(5, 50, 5) #star 5 end 50 step by 5
for i in z:
    print('i is {}'.format(i))

# a dictionary:
d = {'one': 1, 'two': 2, 'three': 3}
d['three'] = 42 #mutable!
for k, v in d.items():
    print('k: {}, v: {}'.format(k,v))