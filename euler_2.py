#! /usr/bin/env python

def fibgen(limit = 10):
    last_x, x = 1, 1
    while x < limit:
        yield x
        last_x, x = x, last_x
        x = last_x + x

print sum([x for x in fibgen(4000000) if x % 2 == 0])
