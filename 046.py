"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

import math

def is_prime(n):
    p = 3
    while p < n ** 0.5 + 1:
        if n % p == 0: return False
        p += 2
    return True

odd_primes = []

found = False
i = 3
while not found:
    if is_prime(i):
        odd_primes.append(i)
        i += 2
    else:
        for s in xrange(1, int(i**.5) +1):
            if i - 2*s**2 in odd_primes:
                i += 2
                break
        else: 
            found = True
            print i