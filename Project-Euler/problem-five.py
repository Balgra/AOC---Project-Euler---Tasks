# 2520 is the smallest number that can be divided by each of the numbers 1 from 10 to  without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Get gratest common divisor between two numbers

def great_common_div(a, b):
    while b:
        a, b = b, a % b
    return a

result = 1

for i in range(1, 21):
    result = result * i // great_common_div(result, i)

print(result)