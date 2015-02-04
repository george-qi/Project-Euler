"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def is_prime(n):
	if n % 2 == 0: return False
	p = 3
	while p < n ** 0.5 + 1:
		if n % p == 0: return False
		p += 2
	return True

def sum_primes(n):
	number = 3
	sum = 2
	while number < n:
		if is_prime(number): sum += number
		number += 2
	return sum

print sum_primes(2000000)
