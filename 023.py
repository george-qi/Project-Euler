"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

# find abundants

def is_abundant(n):
	divisors = []
	for i in xrange(1, n//2+1):
		if n % i == 0: divisors.append(i)
	return sum(divisors) > n

abundants = [ele for ele in xrange(2, 28124) if is_abundant(ele)]
abundants_dict = dict.fromkeys(abundants, 1)

total = 0

for i in xrange(1, 28124):
	sum_exists = False
	for num in abundants:
		if num > i: break
		if abundants_dict.get(i - num):
			sum_exists = True
			break
	if not sum_exists:
		total += i

print total