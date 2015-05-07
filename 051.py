"""
Project Euler Problem 51
========================

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

# Naive as I try a lot of of the same families multiple times.
# Another solution would be to go through the entire primelist and check

import math
from common_functions import is_prime

def replace_digit(n):
	'Returns True if number is part of an 8 prime value family'
	string = str(n)
	length = len(string)
	digits = map(int, string)
	unique = list(set(map(int, string)))
	for d in unique:
		count = 10
		if not is_prime(n): count -= 1
		for i in xrange(10):
			if i != d: 
				new_digits = [str(i) if ele == d else str(ele) for ele in digits]
				new = int(''.join(new_digits))
				# disregard 0's in the beginning that shorten length
				if new == 0 or math.floor(math.log10(new)) + 1 < length: count -= 1
				else: 
					if not is_prime(new): count -= 1
			if count < 8: break
		if count == 8: return True
	return False

i = 100000
while not replace_digit(i):
	i += 1
print i