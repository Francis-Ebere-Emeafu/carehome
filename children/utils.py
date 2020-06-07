import datetime
from django.utils import timezone



def get_time_constants():
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    timeNow = datetime.datetime.now()
    dateNow = timeNow.date()
    dayNow = dateNow.weekday()
    day_of_week = weekDays[dayNow]

    today = timezone.now()
    hour = today.hour
    if hour < 12:
        daytime = 'AM'
        greeting = 'Good morning'
    elif hour < 18:
        daytime = 'PM'
        greeting = 'Good afternoon'
    else:
        daytime = 'PM'
        greeting = 'Good evening'

    return (day_of_week, daytime, greeting)
