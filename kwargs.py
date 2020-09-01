# keyword arguments

def main():
    x = dict(Buffy = 'meow', Zilla = 'grrr', Angel = 'rawr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('meh')

if __name__ == '__main__': main()