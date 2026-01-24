

# Calculate the sum of digits of 2^1000
#insert(0,val)
number_stringified=[1]

for i in range(1,1001):
    carry_over=0

    for j in range(0,len(number_stringified)):

        aux = number_stringified[j] * 2 + carry_over

        number_stringified[j] = aux % 10 
        
        carry_over = aux // 10 

    if carry_over != 0:

        number_stringified.append(carry_over)
            
sum=0
for values in number_stringified:

    sum+=values

print(sum)




