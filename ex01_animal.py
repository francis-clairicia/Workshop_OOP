#!/usr/bin/env python3
# Ex01:
# Create a "Animal" class which can have a species, a name, and a sound

class Animal:
    def __init__(self):
        pass


def main():
    dog = Animal("dog", "Henry", "Wouaf")
    cat = Animal("cat", "Kevin", "Miaou")
    dog.speak()  # prints 'Henry says Wouaf
    cat.speak()  # prints 'Kevin says Miaou


if __name__ == "__main__":
    main()
