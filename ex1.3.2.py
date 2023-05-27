import math


def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, math.isqrt(number) + 1))


print(is_prime(42))
print(is_prime(43))
