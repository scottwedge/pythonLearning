def main():
    game = [ 'rock', 'paper', 'scissors' ]
    i = game.index('paper')
    print(i)
    game.append('something-else')
    game.insert(2, 'something-here')
    game.remove('something-else') # or .pop to pop from end of list
    # or pop(index) for specific index ie .pop(3)
    print(', '.join(game))
    print(len(game))
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()

# a tuple would look the same, exept for ( ) instead!
# a tuple is immutable

# list comprehension

def list_compr():
    seq = range(11)
    # seq2 = [x * 2 for x in seq]
    # seq2 = [x for x in seq if x % 3 != 0]
    # seq2 = [(x, x**2) for x in seq]
    # from math import pi
    # seq2 = [round(pi,i) for i in seq]
    seq2 = { x for x in 'superduper' if x not in 'pd' }
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

list_compr()    