"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

def both_palindrome(num):
	if str(num) != str(num)[::-1]: return False
	if bin(num)[2:] != bin(num)[2:][::-1]: return False
	return True

print sum([i for i in range(1000000) if both_palindrome(i)])