#! /usr/bin/env python

def prime_with(x, s):
    """ Is x prime with every element in s? """
    for i in s:
        if x % i == 0:
            return False
    return True

def prime_gen():
    """ Generator for primes up to 1000000000. """
    o = []
    x = 2
    while True:
        if prime_with(x, o):
            yield x
            o.append(x)
        x += 1

def nth_prime(n):
    p = prime_gen()
    for i in xrange(n - 1):
        p.next()
    return p.next()

print nth_prime(1)
print nth_prime(6)
print nth_prime(10001)
