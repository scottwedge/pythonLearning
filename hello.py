#!/usr/bin/env python3

import platform

x = 42
hello = 'hello world. {}'.format(x)

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('woohoo Python yay!')
    print('hello world. {}'.format(x))
    print(hello)
    print(f'hello world. {x}')
if __name__ == '__main__': main()
