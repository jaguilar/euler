#! /usr/bin/env python

from math import *

def prime_with(x, s):
    """ Is x prime with every element in s? """
    for i in s:
        if x % i == 0:
            return False
    return True

def prime_gen():
    """ Generator for primes up to 1000000000. """
    o = []
    for x in xrange(2, 1000000000):
        if prime_with(x, o):
            yield x
            o.append(x)

def factor(x):
    """ A list of x's prime factors. """
    factors = []
    for prime in prime_gen():
        while x % prime == 0:
            x = x / prime
            factors.append(prime)
        if x == 1:
            break
    return factors

print max(factor(600851475143))

