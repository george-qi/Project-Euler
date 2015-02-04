"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

def fact(n):
	prod = 1
	for i in range(2, n+1): prod *= i
	return prod

print sum([int(char) for char in str(fact(100))])