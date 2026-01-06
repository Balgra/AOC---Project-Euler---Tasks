# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is   9009.

# Find the largest palindrome made from the product of two 3-digit numbers.

max = 0
for i in range(1000,99,-1):

    for j in range(i,99,-1):

        prod = i * j

        if prod <= max:
            break
        
        if str(prod) == str(prod)[::-1]:
            max = prod

print(max)

        

