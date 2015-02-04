"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

from operator import mul

string = ''.join([str(i) for i in range(1, 200000)])

def d_n(digit):
	return string[digit - 1]

print reduce(mul, [int(d_n(10 ** i)) for i in range(7)])