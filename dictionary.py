def main():
    animals = dict(kitten = 'meow', puppy = 'ruff', lion = 'grrr', dragon = 'rawr')
    print_dict(animals)
    # for v in animals.values(): print(v)
    # for k in animals.keys(): print(k)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')
    # for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()