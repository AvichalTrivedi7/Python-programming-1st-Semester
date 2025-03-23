import calendar
year=input("Enter year in YYYY format: ")
month=input("Enter month in MM format: ")
if year.isdigit and month.isdigit:
    year=int(year)
    month=int(month)
    cal=calendar.month(year,month)
    print(cal)
else:
    print("You've entered in wrong format, try again")
#other notable functions ---> 
#calendar.calendar(year)     {entire year}
#calendar.weekend(yyyy,mm,dd)     {checks if weekday (gives 0,1)}
#calendar.isleap(yyyy)     {checks if the year mentioned is a leap}
