# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

# bitwise operators
# <<, >>, &, |, ~, and ^ 

# comparison operators
# < > <= >= == !=

# boolean operators
# and, or, not, in, not in, is, is not

x = ['bear', 'bunny', 'tree', 'sky', 'rain']
y = 'sky'

if y in x:
    print('yes')

if y is x[3]:
    print('yes')
print(id(x[3]))
print(id(y))
# Same id! :D

#operator precedence is mostly like math
#but best to use () to specify precedence we want