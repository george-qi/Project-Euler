"""
Project Euler Problem 25
========================

The Fibonacci sequence is defined by the recurrence relation:

  F[n] = F[n[1]] + F[n[2]], where F[1] = 1 and F[2] = 1.

Hence the first 12 terms will be:

  F[1] = 1
  F[2] = 1
  F[3] = 2
  F[4] = 3
  F[5] = 5
  F[6] = 8
  F[7] = 13
  F[8] = 21
  F[9] = 34
  F[10] = 55
  F[11] = 89
  F[12] = 144

The 12th term, F[12], is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

n = 2
fib_values = [1,1]

while len(str(fib_values[n-1])) < 1000:
    fib_values.append(fib_values[n-1] + fib_values[n-2])
    n += 1

print n

# def gen_fib(n):
#     fib_values = [1,2]
#     for i in range(2, n+1):
#         fib_values.append(fib_values[i-1] + fib_values[i-2])
#     return fib_values[n]

# n = 1

# while len(str(gen_fib(n))) < 1000: n += 1

# print n