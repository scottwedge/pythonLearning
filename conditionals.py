x = 42

if x == 42:
    print('true')
elif x == 55:
    print('false')


#identity: x is y, x is not y (true if the same object)
#membership: x in y, x not in y (if var is a member of a collection)
#ternary only avail in new python

hungry = True
x = 'feed bear' if hungry else "don't"
print(x)