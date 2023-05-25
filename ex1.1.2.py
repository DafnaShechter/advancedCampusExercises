def double_letter(my_str):
    return ''.join(map(lambda c: c * 2, my_str))


print(double_letter("python"))
print(double_letter("we are the champions!"))
