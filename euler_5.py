#! /usr/bin/env python

def has_factors(x, factors):
    for f in factors:
        if not x % f == 0:
            return False
    return True

def remove_redundant_factors(x, factors):
    print x
    for f in reversed(factors):  # Remove largest factors first.
        while x % f == 0 and has_factors(x / f, factors):
            x = x / f
    return x

factors = range(2, 21)
x = reduce(lambda x, y: x*y, factors)
print remove_redundant_factors(x, factors)
