"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numer and
denom.

If the product of these four fractions is given in its lowest common
terms, find the value of the denom.
"""

def gcd(a, b):
	while b: a, b = b, a % b
	return a

numerator = 1
denominator = 1

for numer in map(str, xrange(10, 100)):
	for denom in map(str, xrange(int(numer)+1, 100)):
		if numer[1] == denom[1] and numer[1] == '0': continue
		for i in xrange(2):
			for j in xrange(2):
				if numer[i] == denom[j] and denom[(j+1)%2] != '0':
					if float(numer) / float(denom) == float(numer[(i+1)%2]) / float(denom[(j+1)%2]):
						numerator, denominator = numerator * int(numer), denominator * int(denom)

print denominator / gcd(numerator, denominator)