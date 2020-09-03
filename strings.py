# string methods:
# .upper()
# .lower()
# .capitalise()
# .title()
# .swapcase()
# .casefold()

# a string is immutable
# so after method it is a new/different object
# method creates a new object

# formatting:
x = 42
print(f'string interpolation!: x is: {x}')

# decimal places: {:.2f} --> number for how many
y = 42 * 747 * 1000
print(f'number y is: {y:.2f}')

# split and seperate strings:
# 
# string.split() --> makes a list, ignoring long spaces
# join with 'joiner'.join(string)
# ie: ','.join(string)