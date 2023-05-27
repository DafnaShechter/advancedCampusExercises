def parse_ranges(ranges_string):
    ranges = (range(int(start), int(stop) + 1) for start, stop in (r.split('-') for r in ranges_string.split(',')))
    return (num for r in ranges for num in r)


# Test the parse_ranges function
print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
