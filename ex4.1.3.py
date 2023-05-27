def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    number = n + 1
    while True:
        if is_prime(number):
            return number
        number += 1


# Test the first_prime_over function
print(first_prime_over(1000000))
