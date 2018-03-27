# This program will introduce about the use of Date & Time Library
import datetime
import time
#today function
currentDate = datetime.date.today()
print(currentDate.strftime('%a, %d, %B, %Y'))
print()
print(currentDate.year)
print()
print(currentDate.day)
print()
print(currentDate.month)
print()
now = datetime.datetime.now()
print(str(now))

BirthDay = input("Enter your birth date ")
BirthDay = datetime.datetime.strptime(BirthDay, "%m/%d/%Y").date()
print(BirthDay)
difference = BirthDay - currentDate
print(difference)
