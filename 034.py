"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def fact(n):
	prod = 1
	for i in range(2, n+1): prod *= i
	return prod

factorials = [fact(i) for i in range(10)]

def is_curious(n):
	return n == sum([factorials[int(char)] for char in str(n)])

print sum([i for i in xrange(10, 2177286) if is_curious(i)])