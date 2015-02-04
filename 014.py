"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
	13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def length_collatz(start):
	count = 1
	while start != 1:
		if start % 2 == 0:
			start = start / 2
			count +=1
		else:
			start = 3 * start + 1
			count +=1
	return count

max = 0
max_start = 0
for num in range(1, 1000000):
	if length_collatz(num) > max:
		max = length_collatz(num)
		max_start = num

print max_start