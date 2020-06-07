# import Python's datetime module
import datetime


# weekdays as a tuple
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# Find out what day of the week is this year's Christmas
timeNow = datetime.datetime.now()
dateNow = timeNow.date()
dayNow = dateNow.weekday()
dayOfWeek = weekDays[dayNow]
print(dateNow)
print(dayNow)
print(dayOfWeek)
