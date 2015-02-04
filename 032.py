"""
Project Euler Problem 32
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

def has_pandigital(n):
	for a in range(1, n//2 + 1):
		if n % a == 0:
			if ''.join(sorted(str(a) + str(n/a) + str(n))) == '123456789':
				return True
	return False

print sum([num for num in range(1000, 10000) if has_pandigital(num)])