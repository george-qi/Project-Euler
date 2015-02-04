"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

import math

def number_solutions(n):
	count = 0
	for hyp in range(n // 3, n // 2):
		for side in range(1, hyp):
			if side ** 2 + (n - hyp - side) ** 2 == hyp ** 2: count += 1
	# overcounts by a factor of 2
	return count /2

print max([(number_solutions(i), i) for i in range(1, 1000)])[1]