# Generator function to generate seconds
def gen_secs():
    for sec in range(60):
        yield sec


# Generator function to generate minutes
def gen_minutes():
    for minute in range(60):
        yield minute


# Generator function to generate hours
def gen_hours():
    for hour in range(24):
        yield hour


# Generator function to generate time in the format HH:MM:SS
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


# Generator function to generate years starting from a given year
def gen_years(start=2023):
    while True:
        yield start
        start += 1


# Generator function to generate months
def gen_months():
    for month in range(1, 13):
        yield month


# Generator function to generate days based on the month and leap year status
def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    yield days_in_month[month]


# Generator function to generate dates in the format DD/MM/YYYY HH:MM:SS
def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


# Generate and print 5 dates after skipping 1 million iterations each time
gt = gen_date()
for k in range(5):
    for i in range(1000000):
        next(gt)
    print(next(gt))
