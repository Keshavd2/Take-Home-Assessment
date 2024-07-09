import datetime


def calculateNumDays(day_1, month_1, year_1, day_2, month_2, year_2):
    
    num_days_month_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
    num_days_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    total_days_after_month = [365, 334, 306, 275, 245, 214, 184, 153, 122, 92, 61, 31, 0]
    total_days_before_month = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

    num_days = 0
    
    num_days += (year_2 - year_1 + 1) * 365                             #number of days for years
    num_leap_days = (year_2 - year_1) // 4                              #number of leap days in that span of time
    if year_1 % 4 == 0 and year_2 % 4 == 0:                              #extra leap day
        num_leap_days += 1
    elif year_1 % 4 == 0 and year_2 % 4 != 0:
        num_leap_days += 1
    elif year_1 % 4 != 0 and year_2 % 4 == 0:
        num_leap_days += 1
    elif year_2 % 4 != 0 and year_1 % 4 != 0:
        if year_2 - year_1 > 2:
            num_leap_days += 1
        if year_2 - year_1 == 2 and (year_1 + 1) % 4 == 0:
            num_leap_days += 1
    num_days += num_leap_days
    
    if year_2 % 4 == 0:
        num_days -= total_days_after_month[month_2]                     #substract months after month_2 
        num_days -= num_days_month_leap[month_2 - 1] - day_2            #substract days after day_2
        if month_2 < 2:                                                 #substract leap day
            num_days -= 1
    else:
        num_days -= total_days_after_month[month_2]                     #substract months after month_2
        num_days -= num_days_month[month_2 - 1] - day_2                 #substract days after day_2

    num_days -= day_1                                                   #substract days before day_1
    if month_1 == 1:
        return num_days

    if year_1 % 4 == 0:
        num_days -= total_days_before_month[month_1 - 2]                #substract months before month_1
        if month_1 > 2:                                                 #substract leap day
            num_days -= 1
    else:
        num_days -= total_days_before_month[month_1 - 2]                #substract months before month_1

    return num_days                                                     #returns total number of days in between

def NumWeekdays(day_1, month_1, year_1, day_2, month_2, year_2):
    day_difference = calculateNumDays(day_1, month_1, year_1, day_2, month_2, year_2)
    add_days_back = 0
    sub_days_back = 0
    if date1.weekday() < 5:                         #if day is a weekday
        add_days_back = 4 - date1.weekday() + 1     
    if date2.weekday() < 5:                         #if day is a weekday
        sub_days_back = 4 - date2.weekday()

    day_difference += (date1.weekday() - 6) + (6 - date2.weekday())             #make both dates sunday, 
    num_week_days = (day_difference * (5/7)) + add_days_back - sub_days_back    #then calculate week days and then add back and substract days that were used
    return num_week_days                                                        #returns total number of week days (i.e. Mon - Fri)


# print("\n\n------- Enter Date 1 details -------")               #request user input
# year_1 = input("Enter Year (Number): ")                         #request year
# month_1 = input("Enter Month (Number): ")                       #request month
# day_1 = input("Enter Month Day (Number): ")                     #request day of month

# print("\n------- Enter Date 2 details -------")                 #request user input
# year_2 = input("Enter Year (Number): ")                         #request year
# month_2 = input("Enter Month (Number): ")                       #request month
# day_2 = input("Enter Month Day (Number): ")                     #request day of month


day_1, month_1, year_1 = 31, 1, 2024  #type-cast data types
day_2, month_2, year_2 = 4, 1, 2024

day_1, month_1, year_1 = int(day_1), int(month_1), int(year_1)  #type-cast data types
day_2, month_2, year_2 = int(day_2), int(month_2), int(year_2)  

date1 = datetime.datetime(year_1, month_1, day_1)       #create dateime object with date info for date 1
date2 = datetime.datetime(year_2, month_2, day_2)       #create dateime object with date info for date 2

if date1 > date2:                                       #make sure dates are chronologically ordered
    date1, date2 = date2, date1
    day_1, month_1, year_1, day_2, month_2, year_2 = day_2, month_2, year_2, day_1, month_1, year_1

num_week_days = NumWeekdays(day_1, month_1, year_1, day_2, month_2, year_2)                 #total number of week days

print("The number of Week Days: %s" % num_week_days)        #print results



