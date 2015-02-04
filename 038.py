"""
Project Euler Problem 38
========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def has_pandigital(n, list):
	if sorted(''.join(map(str, [n * ele for ele in list]))) \
	== [str(i) for i in range(1,10)]:
		return True
	return False

def produce_pandigital(n, list):
	return int(''.join(map(str, [n * ele for ele in list])))

max = 0

# integer cannot have more than 5 digits
for i in range(1, 10000):
	for length in range(2, 9 // len(str(i)) + 1):
		seq = range(1, length + 1)
		if has_pandigital(i, seq) and produce_pandigital(i, seq) > max:
			max = produce_pandigital(i, seq)

print max