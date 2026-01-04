
# A number is a perfect square, or a square number, if it is the square of a positive integer.
# For example,  is a square number because  5^2 = 5 x 5 = 25  ; it is also an odd square.

# The first 5 square numbers are: 1, 4, 9, 16, 25 , and the sum of the odd squares is  1 + 9 + 25 =35.

# Among the first 886 thousand square numbers, what is the sum of all the odd squares?


x = 886000
s=0
for i in range(1,x+1,2) :

    s += i * i

print(f'A more programming approach: {s}')



n = x // 2 
total_sum = n * (4 * n * n - 1) // 3 
print(f"A more mathematic approach : {total_sum}")
