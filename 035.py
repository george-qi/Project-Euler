"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def is_prime(n):
	if n == 2: return True
	if n % 2 == 0: return False
	p = 3
	while p < n ** 0.5 + 1:
		if n % p == 0: return False
		p += 2
	return True

def is_circular(n):
	if not is_prime(int(n)): return False
	for index in range(1, len(n)):
		if not is_prime(int(n[index:] + n[:index])): return False
	return True

print len([i for i in map(str, xrange(2, 1000000)) if is_circular(i)])