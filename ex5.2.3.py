from itertools import combinations

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
target_amount = 100

options = set()

for r in range(1, len(bills) + 1):
    for combination in combinations(bills, r):
        if sum(combination) == target_amount:
            options.add(tuple(sorted(combination)))

# Print all the options
for option in options:
    print(option)

# Count the number of options
num_options = len(options)
print("Number of options:", num_options)
