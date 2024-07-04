import calendar

a = calendar.Calendar()
print(a.monthdays2calendar(2024,7))

num_days_month = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
num_days_month_leap = {0:31, 1:29, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}

year_difference = 2024 - 2022
month_difference = 0


def calculateNumDays(day_1, month_1, year_1, day_2, month_2, year_2):
    num_days = 0
    
    while (year_1 <= year_2):
        if year_1 % 4 == 0:
            num_days += 366
        else:
            num_days += 365
        year_1 += 1

    for month_index in range(month_2, 12):
        if year_2 % 4 == 0:
            num_days -= num_days_month_leap[month_index]
        else:
            num_days -= num_days_month[month_index]

    for month_index in range(0, month_1):
        if year_1 % 4 == 0:
            num_days -= num_days_month_leap[month_index]
        else:
            num_days -= num_days_month[month_index]

    if year_2 % 4 == 0:
        num_days -= num_days_month_leap[month_2 - 1] - day_2
    else:
        num_days -= day_1 - 1

    return num_days

    print(calculateNumDays(3,7,2024, 7,7,2024))



    