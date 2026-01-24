
dict = {1: 1}

def generate_length(n):
    if n in dict:
        return dict[n]

    if n % 2 == 0:
        length = 1 + generate_length(n // 2)
    else:
        length = 1 + generate_length(3*n + 1)

    dict[n] = length
    return length


max_length = 0
start_number = 0

for i in range(1, 1000000):

    length = generate_length(i)
    if length > max_length:
        max_length = length
        start_number = i

print(start_number, max_length)