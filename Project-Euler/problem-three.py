
# The prime factors of 13159 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?
import math

#basic solution but since we are parsing the elements so much it's inefficient.
# for x in range(int(math.sqrt(600851475143)),2,-1): 
    
#     flag = False

#     for i in range(2,int(math.sqrt(x)) + 1):

#         if x % i == 0 :
#             flag = True
#             break

#     if flag == False and 600851475143 % x == 0 :
#         print(x)
#         break


#A solution which is way faster 

n = 600851475143
factor = 2
largest = 1

while factor * factor <= n :

    while n % factor == 0 :
        largest = factor
        n = n // factor
    
    factor += 1

if n > 1 :
    largest = n

print(largest)