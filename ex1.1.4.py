def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


print(sum_of_digits(104))
