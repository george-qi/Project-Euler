"""
Project Euler Problem 48
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

mod = 10**10
sum = 0

for i in xrange(1,1001):
	sum += i**i % mod

print sum % mod