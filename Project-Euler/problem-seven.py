# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.

# What is the 10001 st prime number?

import math

n = 0                 # number of primes found
prime_nr = 2          # number being tested

while n != 10001:

    rez = 0
    for i in range(2, int(math.sqrt(prime_nr)) + 1):
        if prime_nr % i == 0:
            rez = 1
            break

    if rez == 0:
        n += 1

    if n == 10001:
        print(prime_nr, n)
        break

    prime_nr += 1

