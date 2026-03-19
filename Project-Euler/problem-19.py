month_days = {
    1:31, 2:28, 3:31, 4:30,
    5:31, 6:30, 7:31, 8:31,
    9:30, 10:31, 11:30, 12:31
}

day_of_week = 0   # 0 = Monday (1 Jan 1900)

sunday_count = 0

for year in range(1900, 2001):

    for month in range(1,13):

        if year >= 1901 and day_of_week == 6:
            sunday_count += 1

        days = month_days[month]


        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days += 1

        day_of_week = (day_of_week + days) % 7

print(sunday_count)