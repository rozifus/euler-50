#!/usr/bin/env python

"""Project Euler Problem 1

>>> answer()
233168
"""

def answer():
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

if __name__ == "__main__":
    print( answer() )

