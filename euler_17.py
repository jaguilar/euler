#! /usr/bin/env pypy

def len_of_series(x): return sum(map(len, x))

digits = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine')
teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen',
         'nineteen')
tens = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety')

def make_word_num(x):
    if x == 1000:
        return 'onethousand'
    out = ''
    if x / 100 > 0:
        out = out + digits[x/100] + 'hundred'
    if x % 100 > 0 and len(out) > 0:
        out = out + 'and'
    x = x % 100
    if x == 0:
        return out
    if 10 <= x < 20:
        out += teens[x-10]
        return out
    out += tens[x / 10]
    out += digits[x % 10]
    return out

def solve(v):
    print(sum(map(lambda x: len(make_word_num(x)), v)))

solve(xrange(1, 1001))
