NAMES = open(r'C:\names.txt').read().splitlines()


def a():
    # Find the name with the maximum length and print it
    print(max(NAMES, key=len))


def b():
    # Calculate the total sum of lengths of all names and print it
    print(sum(len(name) for name in NAMES))


def c():
    # Find the shortest length of names and print all names with that length
    shortest_length = min(len(name) for name in NAMES)
    shortest_names = [name for name in NAMES if len(name) == shortest_length]
    print('\n'.join(shortest_names))


def d():
    # Write the lengths of all names to a file
    name_lengths = [str(len(name)) for name in NAMES]
    with open(r'C:\name_length.txt', 'w') as file:
        file.write('\n'.join(name_lengths))


def e():
    # Filter names based on user input length and print the filtered names
    length = int(input('Enter name length: '))
    filtered_names = [name for name in NAMES if len(name) == length]
    print('\n'.join(filtered_names))


def main():
    # Perform operations a, b, c, d, and e
    a()
    b()
    c()
    d()
    e()


if __name__ == '__main__':
    main()
