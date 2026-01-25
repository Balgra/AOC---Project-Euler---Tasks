

# For number from 1 to 1000  inclusive were written out in words, how many letters would be used?

word_dict= [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
word_dict20_90 = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]


sum = 0

for value in word_dict20_90:

    word_dict.append(value)
    for i in range(0,9):
        word_dict.append(str(value + word_dict[i]))

for i in range(0,9):

    word_dict.append(str(word_dict[i] + 'hundred'))

    for k in range(0, 99):
        word_dict.append(str(word_dict[i] + 'hundredand' + word_dict[k]))

word_dict.append('onethousand')
print(word_dict)
for values in word_dict:

    sum += len(values)

print(sum)

