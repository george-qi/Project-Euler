"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

def gcd(a, b):
	while b: a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd(a,b)

def lcmm(*args):
	return reduce(lcm, args)

print lcmm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)