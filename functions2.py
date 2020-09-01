# def main():
#     x = [5] #a list, mutable!
#     kitten(x)
#     print(f'in main: x is {x}')

# def kitten(a):
#     a[0] = 3
#     print('meow')
#     print(a)

def main():
    kitten('yes', 'args')

def kitten(*args): #it is convention to call them args
    if len(args):
        for s in args:
            print(s)
    else: print('nah')

if __name__ == '__main__': main()