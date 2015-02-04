"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numer. The decimal representation of
the unit fractions with denoms 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""

def cycle_length(d):
	if d % 2 == 0: return cycle_length(d / 2)
	if d % 5 == 0: return cycle_length(d / 5)
	length = 1
	while True:
		if (10 ** length - 1) % d == 0: return length
		else: length += 1	

# doesn't use fancy math
def cycle_length2(d):
    remainder_list = []
    quotient_count = 0
    remainder = 1

    while remainder:
        remainder = remainder % d
        if remainder in remainder_list:
            return quotient_count - remainder_list.index(remainder)
        remainder_list.append(remainder)
        remainder *= 10
        quotient_count += 1

print max([(cycle_length(d), d) for d in range(1, 1001)])[1]