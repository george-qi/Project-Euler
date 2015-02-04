"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""

count = 1
def fact(n):
	prod = 1
	for x in xrange(2, n+1): prod = prod * x
	return prod

def find_permutation(nums, n):
	perm = ""
	while len(nums) > 0:
		divider = fact(len(nums)-1)
		index = n / divider
		n = n % divider
		perm += str(nums[index])
		nums.remove(nums[index])
	return perm

print find_permutation(range(0,10), 999999)
