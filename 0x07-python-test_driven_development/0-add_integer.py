#!/usr/bin/python3

def add_integer(a, b=98):
    """ return a + b """
    if not isinstance(a, (int or float)):
        raise TypeError('a must be integer')
    if not isinstance(b, (int or float)):
        raise TypeError('b must an integer')
    return int(a) + int(b)
