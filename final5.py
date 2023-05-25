class IDIterator:
    def __init__(self, id_):
        self.id_ = id_

    def __iter__(self):
        return self

    def __next__(self):
        if self.id_ == 999999999:
            raise StopIteration
        self.id_ += 1
        while not check_id_valid(self.id_):
            self.id_ += 1
        return self.id_


def check_id_valid(id_number):
    """
    Checks the validity of an ID number.

    Args:
        id_number (int): The ID number to check.

    Returns:
        bool: True if the ID number is valid, False otherwise.
    """
    digits = [int(digit) for digit in str(id_number)]
    multiplied_digits = [digit * (2 if i % 2 != 0 else 1) for i, digit in enumerate(digits)]
    summed_digits = [digit if digit < 10 else digit - 9 for digit in multiplied_digits]
    total_sum = sum(summed_digits)
    return total_sum % 10 == 0


def id_generator(id_number):
    """
    Generates the next valid ID number in the range (up to 999999999).

    Args:
        id_number (int): The initial ID number.

    Yields:
        int: The next valid ID number.
    """
    while id_number != 999999999:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number


def main():
    id_number = int(input("Enter ID: "))
    iterator_or_generator = input("Generator or Iterator? (gen/it)? ")

    if iterator_or_generator == "it":
        iterator = IDIterator(id_number)
        next(iterator)  # Skip the first ID number
        for _ in range(10):
            print(next(iterator))
    elif iterator_or_generator == "gen":
        generator = id_generator(id_number)
        next(generator)  # Skip the first ID number
        for _ in range(10):
            print(next(generator))


if __name__ == "__main__":
    main()
