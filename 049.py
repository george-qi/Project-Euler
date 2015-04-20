"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from common_functions import prime_list
from itertools import permutations

primes = prime_list(1000, 10000)
primes.remove(1487)
t = dict.fromkeys(primes, 1)

# print [''.join(ele) for ele in list(permutations('535'))]
# print find_perms('1003')
# def ans():
# 	for p in primes:
# 		nums = []
# 		for perm in set(permutations(str(p))):
# 			print ''.join(perm)
# 			if int(''.join(perm)) in t: 
# 				nums.append(perm)
# 		if len(nums) >= 3: 
# 			print "nums ", nums
# 			return ''.join(sorted(nums))
def ans():
	for p in primes:
		p1, p2 = p + 3330, p + 3330*2
		if p1 in t and p2 in t:
			# print p
			perms = [int(''.join(ele)) for ele in list(permutations(str(p)))]
			# print perms
			if p1 in perms and p2 in perms:
				return str(p) + str(p1) + str(p2)

print ans()

# print "done"

# print find_perms('1001')