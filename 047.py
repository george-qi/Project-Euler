"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from common_functions import prime_list

# smallest number with 4 distinct prime factors is 2*3*5*7 = 210
a = 210
primes = prime_list(2, 1000)

def four_factors(n):
    count = 0
    for p in primes:
        if n % p == 0: count += 1
        if count == 4: return True
        if p >= n: return False

found = False
while not found: 
    if not four_factors(a): a += 1
    elif not four_factors(a+1): a += 2
    elif not four_factors(a+2): a += 3
    elif not four_factors(a+3): a += 4
    else: 
        found = True
        print a
