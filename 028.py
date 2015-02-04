"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

def sum_diagonals(spiral):
	sum = 1
	current_number = 1

	for i in range(1, spiral // 2  + 1):
		for j in range(1, 5):
			sum += current_number + 2 * i
			# print current_number + 2 * i
			current_number += 2 * i

	return sum

print sum_diagonals(1001)