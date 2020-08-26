#!/usr/bin/env python3

def function(n):
    print(n)

function(5)

# and a bit more complex one

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 5
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')

def list_primes():
    print('listing primes:')
    for n in range(100):
            if isprime(n):
                print(n, end=' ', flush=True)
    print()

list_primes()