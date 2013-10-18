#!/usr/bin/env python

"""Project Euler Problem 2

>>> answer()
4613732
"""

def answer():

    result = 0
    a,b = 1,0

    FOUR_MILLION = 4 * 1000 * 1000
    while(a <= FOUR_MILLION):
        if a % 2 == 0:
            result += a
        a,b = b+a, a

    return result

if __name__ == "__main__":
    print( answer() )

