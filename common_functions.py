def gcd(a, b):
	while b: a, b = b, a % b
	return a

def prime_list(min, max):
	sieve = [True] * (max)
	for i in xrange(3, int(max**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*((max-i*i-1)/(2*i)+1)
	if min == 2: return [2] + [i for i in xrange(3,max,2) if sieve[i]]
	return [i for i in xrange(min,max,2) if sieve[i] and i > min]

# AKS 
def is_prime(n):
	if n == 2: return True
	if n == 3: return True
	p, w = 5, 2
	while p * p <= n:
		if n % p == 0: return False
		p += w
		w = 6-w
	return True

def factorial(n):
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