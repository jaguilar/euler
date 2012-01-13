#! /usr/bin/env python

def prime_with(x, s):
    """ Is x prime with every element in s? """
    for i in s:
        if x % i == 0:
            return False
    return True

def prime_gen():
    """ Generator for primes. """
    o = []
    x = 2
    while True:
        if prime_with(x, o):
            yield x
            o.append(x)
        x += 1

s = 0
for i in prime_gen():
    if i < 2000000:
        s += i
    else:
        break
print s
