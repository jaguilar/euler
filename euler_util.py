#! /usr/bin/env pypy

from math import *

memo_primes = [2]
def prime_with(x, s):
    """ Is x prime with every element in s? """
    for i in s:
        if x % i == 0:
            return False
    return True

def prime_gen():
    """ Generator for primes. First yield primes previously generated. """
    for i in memo_primes: yield i
    x = memo_primes[-1] + 1
    
    while True:
        if prime_with(x, memo_primes):
            yield x
            memo_primes.append(x)
        x += 1

def factor_primes(x, iter):
    """ From the contents of iter, find factors of x. """
    factors = []
    for factor in prime:
        while x % factor == 0:
            x = x / factor
            factors.append(factor)
        if x == 1:
            break
    return factors

def factor_all(x):
    for factor in xrange(1, int(sqrt(x)+1)):
        if x % factor == 0:
            yield factor
            yield x / factor
