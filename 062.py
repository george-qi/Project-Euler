"""
Project Euler Problem 62
========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""

import math
from itertools import permutations

# found = False
# n = 400
# while not found:
# 	print n
# 	n += 1
# 	perms = list(set([int(''.join(e)) for e in list(permutations(str(n ** 3)))]))
# 	cubes = []
# 	for p in perms:
# 		c = int(n ** (1/3.0))
# 		if (c**3 == n) or ((c+1)**3 == n):
# 			cubes.append(p)
# 	if len(cubes) == 5:
# 		found = True
# 		print min(cubes)

def find_cube():
	cube_dict = {}
	for i in xrange(10000):
		cube_dict[i] = ''.join(sorted(list(str(i**3))))
	cubes = sorted(list(cube_dict.values()))

	for i in xrange(0, len(cubes)):
		if cubes[i:i+5] == [cubes[i]] * 5:
			for key, val in cube_dict.items():
				if val == cubes[i]: return key ** 3

print find_cube()
