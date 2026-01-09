# The sum of the primes below 10  is 2 + 3 + 5 + 7= 17.

# Find the sum of all the primes below two million.

import math

sum = 5

for i in range(4,2000000):

    flag = True

    for j in range(2, int(math.sqrt(i) + 1)):

        if i % j == 0:

            flag = False
            break

    if flag:

        sum += i

print(sum)

    
   