# datetime is the builtin Python module
from datetime import date
from datetime import time
from datetime import datetime

# Getting the Current Date and Time with datetime

# datetime.date: Stores the day, month and year or a date
print(date.today())

# datetime.time: Stores the time in hours, minutes, seconds, and microseconds. This information is independent from any date
print(time.hour)

# datetime.datetime: Stores both date and time attributes
print(datetime.today())

current_datetime = datetime.now()
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

# Getting the Current Date
current_date = datetime.now().today()
print(current_date)

current_date = date.today()
print(current_date)

# Getting the Current Time
current_time = datetime.now().time()
print(current_time)
