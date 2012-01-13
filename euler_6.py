#! /usr/bin/env python

from math import *

def f(r):
    return abs(reduce(lambda x, y: x + y*y, r) - sum(r)*sum(r))

print(f(range(1, 101)))
