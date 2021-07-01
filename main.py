#Python program to display calendar
# import module
import calendar

yy = 2021
mm = 10

# to ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar

print(calendar.month(yy, mm))
