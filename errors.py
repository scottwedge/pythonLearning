import sys

# def main():
#     try:
#         # x = int('foo')
#         y = 5/0
#     except ValueError:
#         print('I caught a value error!')
#     except:
#         print(f'an error occured: {sys.exc_info()}') #tells us which error
#     # except ZeroDivisionError:
#     #     print('no dividing by zero!')
#     else:
#         print('good stuff')

# full example from functions: 
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

def main():
    for i in inclusive_range(25):
        print(i, end = ' ', flush = True)
    print()

if __name__ == '__main__': main()