#! /usr/bin/env pypy

import euler_util

def tri_nums():
    x = 1
    n = 0
    while True:
        n = n + x
        x += 1
        yield n

for n in tri_nums():
    f = list(euler_util.factor_all(n))
    if len(f) > 500:
        print n
        print sorted(f)
        break
