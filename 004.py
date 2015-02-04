"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
	palin_str = str(num)
	palin = True
	index = 0
	while palin and index < len(palin_str):
		if palin_str[index] != palin_str[len(palin_str) - 1 - index]:
			palin = False
		index += 1
	return palin

max = 0

for num_1 in range(999, 99, -1):
	for num_2 in range(999, 99, -1):
		if is_palindrome(num_1 * num_2) and (num_1 * num_2) > max:
			max = num_1 * num_2

print max
