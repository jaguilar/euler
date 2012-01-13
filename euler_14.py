#! /usr/bin/env pypy

def collatz_seq(x):
    while x != 1:
        yield x
        if x % 2 == 0:
            x = x/2
        else:
            x = 3 * x + 1
    yield x

best = []
for i in xrange(1, 1000000):
    l = list(collatz_seq(i))
    if len(l) > len(best):
        best = l
print len(best)
print best
        
