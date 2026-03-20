
number_dict = {}

for i in range(1,10001):
    sum = 0
    for j in range(1, i//2 + 1):

        if i % j == 0:
            sum += j

    number_dict[i] = sum


sum = 0
for keys, values in number_dict.items():

    if values in number_dict and number_dict[values] == keys and values != keys:
        sum += keys

print(sum)