#! /usr/bin/env python
from math import *
m = 1001
def c(a,b): return sqrt(a*a+b*b)
print [a * b * c(a, b) for a in xrange(1, m) for b in xrange(a, m)
       if a + b + c(a, b) == 1000]
