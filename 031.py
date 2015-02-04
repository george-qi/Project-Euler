"""
Project Euler Problem 31
========================

In England the currency is made up of pound, L, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).

It is possible to make L2 in the following way:

  1 * L1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can L2 be made using any number of coins?
"""

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def find_ways(coins, money):
	count = 0
	new_coins = coins[1:]
	max_number = money / coins[0]
	if len(new_coins):
		for i in range(max_number, -1, -1):
			new_money = money - (i * coins[0])
			if new_money == 0: count += 1
			else: count += find_ways(new_coins, new_money)
	else: count = 1
	return count

print find_ways(coins, 200)