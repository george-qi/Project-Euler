"""
Project Euler Problem 52
========================

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

def same_digits(a, b):
	return sorted(str(a)) == sorted(str(b))

def valid(n):
	if not same_digits(n, 2*n): return False
	if not same_digits(n, 3*n): return False
	if not same_digits(n, 4*n): return False
	if not same_digits(n, 5*n): return False
	if not same_digits(n, 6*n): return False
	return True

i = 1
while not valid(i):
	i += 1
print i