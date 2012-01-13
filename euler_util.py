#! /usr/bin/env pypy

import functools
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

class memoized(object):
   """Decorator that caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned, and
   not re-evaluated.
   """
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      """Return the function's docstring."""
      return self.func.__doc__
   def __get__(self, obj, objtype):
      """Support instance methods."""
      return functools.partial(self.__call__, obj)
