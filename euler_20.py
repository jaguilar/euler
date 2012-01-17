#! /usr/bin/env pypy

def factorial(n):
    o = 1
    while n > 1:
        o = o * n
        n -= 1
    return o

n = factorial(100)
print(n)
print(sum(map(int, str(n))))
