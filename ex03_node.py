# Ex03
# Create a linked list using Node containing a integer data and a reference to the next value

class Node:
    ...


class List:
    ...


def main():
    l = List()
    print(l.head)  # prints None
    l.push_back(5)
    l.push_back(10)
    l.push_back(24)
    l.push_front(32)
    l.push_front(56)
    print(l.size())  # prints '5'
    l.show()  # prints '56 32 5 10 24'
    print(l.sum())  # prints '127'