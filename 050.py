"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from common_functions import prime_list
from common_functions import is_prime

max = 10**6
primes = prime_list(2, max)
sums = [0]

sum, idx = 0, 0
while (sum < max):
	sum += primes[idx]
	sums.append(sum)
	idx += 1

max_prime = 0
for i in range(idx):
	for j in range(i+1, idx):
		diff = sums[j] - sums[i]
		if is_prime(diff) and diff > max_prime: 
			max_prime = diff

print max_prime