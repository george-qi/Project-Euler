"""
Project Euler Problem 63
========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

# not possible for bases 3 or less, 10 or greater
count = 0
for d in xrange(4, 10):
	last = False
	p = 1
	while not last:
		if len(str(d ** p)) == p:
			count += 1
		else: last = True
		p += 1

# include 1, 2, 3
print count + 3