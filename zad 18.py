def sum_digits(number):
    number = str(number)
    sum = 0
    for n in range(0, len(number)):
        sum += int(number[n])
    return sum
print(sum_digits(7182))