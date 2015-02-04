"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

def recursive_find_routes(x, y):
	if x == 20 and y == 20: return 1
	count = 0
	if x < 20: count += find_routes(x+1, y)
	if y < 20: count += find_routes(x, y+1)
	return count

def iter_find_routes(size):
    list = [1] * size
    for idx in range(size):
        for idx2 in range(idx):
            list[idx2] = list[idx2]+list[idx2-1]
        list[idx] = 2 * list[idx - 1]
    return list[size - 1]

print iter_find_routes(20)