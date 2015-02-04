"""
Project Euler Problem 30
========================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

def power_5th(d):
	return d ** 5
powers = map(power_5th, range(10))

def sum_5th(s):
	if int(s) == sum([powers[int(char)] for char in s]): return True
	return False

print sum([i for i in range(2, 1000000) if sum_5th(str(i))])
