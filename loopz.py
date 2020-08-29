#!/usr/bin/env python3

# a fibonnaci while-loop:
# print('fibonnaci magic!')
# a,b = 0,1
# while b < 1000:
#     print(b, end = ' ', flush = True)
#     a, b = b, a + b

# print()

# # a simple & classy for-loop
# words = ['one', 'two', 'three', 'four', 'five']

# for i in words:
#     print(i)

# a while loop
secret = "swordfish"
password = ''
auth = False
count = 0
max = 5

while password != secret:
    count += 1
    if count > max: break # it will stop
    if count == 3: continue # skips 3
    password = input(f"{count}: What's the secret?")
else:
    auth = True
print('Authorized' if auth else 'not authorized')

# careful to resolve the loop so it doesn't go infinite

# a for loop

animals = ['bear', 'chicken', 'cat']

for animal in animals:
    # if animal == 'bear': continue 
    # if animal = 'cat': break 
    print(animal.capitalize()) # testing capitalize function ha
else: 
    print('thats all')
