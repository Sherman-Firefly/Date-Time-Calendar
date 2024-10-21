import calendar


cal = calendar.TextCalendar()


for month in range(1, 13):
    print(cal.formatmonth(2024, month))  
