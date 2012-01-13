#! /usr/bin/env python

def is_palindrome(x):
    s = str(x)
    return s[::-1] == s

print max([i*j for i in xrange(1000) for j in xrange(1000) if is_palindrome(i * j)])
