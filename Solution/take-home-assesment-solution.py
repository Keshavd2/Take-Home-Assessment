import datetime


def calculateNumDays(day_1, month_1, year_1, day_2, month_2, year_2):
    
    num_days_month = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
    num_days_month_leap = {0:31, 1:29, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
    
    num_days = 0
    year = year_1
    
    while (year <= year_2):
        if year % 4 == 0:
            num_days += 366
        else:
            num_days += 365
        year += 1
    
    for month_index in range(month_2, 12):
        if year_2 % 4 == 0:
            num_days -= num_days_month_leap[month_index]
        else:
            num_days -= num_days_month[month_index]
    
    for month_index in range(0, month_1- 1):
        if year_1 % 4 == 0:
            num_days -= num_days_month_leap[month_index]
        else:
            num_days -= num_days_month[month_index]

    if year_2 % 4 == 0:
        num_days -= num_days_month_leap[month_2 - 1] - day_2
    else:
        num_days -= num_days_month[month_2 - 1] - day_2
        
    num_days -= day_1

    return num_days 





print("\n\n------- Enter Date 1 details -------")               #request user input
year_1 = input("Enter Year (Number): ")                         #request year
month_1 = input("Enter Month (Number): ")                       #request month
day_1 = input("Enter Month Day (Number): ")                     #request day of month

print("\n------- Enter Date 2 details -------")                 #request user input
year_2 = input("Enter Year (Number): ")                         #request year
month_2 = input("Enter Month (Number): ")                       #request month
day_2 = input("Enter Month Day (Number): ")                     #request day of month

date1 = datetime.datetime(int(year_1), int(month_1), int(day_1))    #create dateime object with date info for date 1
date2 = datetime.datetime(int(year_2), int(month_2), int(day_2))    #create dateime object with date info for date 2

# date1 = datetime.datetime(2024, 7, 6)
# date2 = datetime.datetime(2024, 7, 6)

if date1 > date2:                       #make sure dates are chronologically ordered
    date1, date2 = date2, date1

day_difference = calculateNumDays(int(day_1), int(month_1), int(year_1), int(day_2), int(month_2), int(year_2))#total number of days in between

add_days_back = 0
sub_days_back = 0
if date1.weekday() < 5:                         #if day is a weekday
    add_days_back = 4 - date1.weekday() + 1     
if date2.weekday() < 5:                         #if day is a weekday
    sub_days_back = 4 - date2.weekday()

day_difference += (date1.weekday() - 6) + (6 - date2.weekday())             #make both dates sunday, 
num_week_days = (day_difference * (5/7)) + add_days_back - sub_days_back    #then calculate week days and then add back and substract days that were used

print("The number of Week Days: %s" % num_week_days)        #print results



