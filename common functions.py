def gcd(a, b):
	while b: a, b = b, a % b
	return a

def is_prime(n):
	if n % 2 == 0: return False
	p = 3
	while p < n ** 0.5 + 1:
		if n % p == 0: return False
		p += 2
	return True

def fact(n):
	prod = 1
	for i in range(2, n+1): prod *= i
	return prod

def is_palindrome(num):
	palin_str = str(num)
	palin = True
	index = 0
	while palin and index < len(palin_str) // 2 + 1:
		if palin_str[index] != palin_str[len(palin_str) - 1 - index]:
			palin = False
		index += 1
	return palin