# If we list all the natural numbers below 10 that are multiples of 3 or 5 ,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Below 1000 is the key part of this solution as even though it's a multiplier of 5 we won't include it
# Parse through all numbers, check if they are multiplier of 3 or 5 then add it to the sum is the answer True

sum = 0
target = 1000

for i in range(target):

    if  i % 3 == 0 or i % 5 == 0:

        sum += i

print(f'Value of the sum is {sum}')