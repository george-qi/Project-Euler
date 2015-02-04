"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

# includes eleven - nineteen
ones_digit = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens_digit = [0,3,6,6,5,5,5,7,6,6]
hundred = 7
thousand = 8

total = ones_digit[1] + thousand  # include 1000 by default

for i in range(1, 1000):
	x = i % 10  # ones digit
	y = (i // 10) % 10  # tens digit
	z = i // 100  # hundreds digit

	if z != 0:
		total += ones_digit[z] + hundred
		if x != 0 or y != 0: total += 3  # and
	if y == 0 or y == 1: total += ones_digit[y * 10 + x]
	else: total += tens_digit[y] + ones_digit[x]

print total
