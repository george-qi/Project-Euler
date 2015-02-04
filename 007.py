"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

def is_prime(n):
	if n % 2 == 0: return False
	p = 3
	while p < n ** 0.5 + 1:
		if n % p == 0: return False
		p += 2
	return True

def get_prime(n):
	prime_count = 1
	prime = 2
	number = 3
	while prime_count < n:
		if is_prime(number):
			prime = number
			prime_count += 1
		number += 2
	return prime

print get_prime(10001)