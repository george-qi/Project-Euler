"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def is_prime(n):
	if n == 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	p = 3
	while p < n ** 0.5 + 1:
		if n % p == 0: return False
		p += 2
	return True

def left_to_right(n):
	for i in range(len(n)):
		if not is_prime(int(n[i:])): return False
	return True

def right_to_left(n):
	for i in range(len(n), 0, -1):
		if not is_prime(int(n[:i])): return False
	return True

count = 0
number = 11
answers = []

while count < 11:
	if left_to_right(str(number)) and right_to_left(str(number)):
		answers.append(number)
		count += 1
	number += 1

print sum(answers)