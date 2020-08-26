#!/usr/bin/env python3

class Duck:
    sound = "Quackie quackie"

    def quack(self):
        print(self.sound)

    def walk(self):
        print("Walks like a duck!")

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
