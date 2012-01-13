#! /usr/bin/env pypy

import euler_util

@euler_util.memoized
def routes(y, x):
    if y == 0 and x == 0: return 1
    if y < 0 or x < 0: return 0
    return routes(y - 1, x) + routes(y, x - 1)

print routes(20, 20)
