integer_data = 1
for i in range(1, 101):
    integer_data = integer_data * i

digit_sum = 0
while integer_data != 0:
    digit_sum += integer_data % 10
    integer_data = integer_data // 10

print(digit_sum)
