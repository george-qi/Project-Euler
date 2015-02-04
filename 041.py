"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# only primes above 2
def is_prime(n):
	if n % 2 == 0: return False
	p = 3
	while p < n ** 0.5 + 1:
		if n % p == 0: return False
		p += 2
	return True

def produce_pandigitals(string, step, list):
	if step == len(string): list.append(''.join(string))
	for i in range(step, len(string)):
		tmp = [char for char in string]
		tmp[step], tmp[i] = tmp[i], tmp[step]
        # recurse on the portion of the string that has not been swapped yet
		produce_pandigitals(tmp, step + 1, list)
	return list

# 8 and 9 digit pandigital primes do not exist
seven_digits = map(int, produce_pandigitals('1234567', 0, []))
print max([num for num in seven_digits if is_prime(num)])