"""
Project Euler Problem 60
========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""

from common_functions import prime_list
from common_functions import is_prime

p = prime_list(3, 10**4)
length = len(p)

def test(p):
    for i in xrange(len(p)-1):
        for j in xrange(i+1, len(p)):
            s1 = int(str(p[i]) + str(p[j]))
            s2 = int(str(p[j]) + str(p[i]))
            if not (is_prime(s1) and is_prime(s2)): return False
    return True

def find_set():
    for c1 in xrange(length-4):
        for c2 in xrange(c1+1, length-3):
            if not test([p[c1], p[c2]]): continue
            for c3 in xrange(c2+1, length-2):
                if not test([p[c1], p[c2], p[c3]]): continue
                for c4 in xrange(c3+1, length-1):
                    if not test([p[c1], p[c2], p[c3], p[c4]]): continue
                    for c5 in xrange(c4+1, length):
                        if test([p[c1],p[c2],p[c3],p[c4],p[c5]]): 
                            print p[c1]+p[c2]+p[c3]+p[c4]+p[c5]
                            return 

find_set()
