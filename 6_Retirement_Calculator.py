# 6. Retirement Calculator
import datetime
year = datetime.date.today().year

cur_age = input("What is your current age? ")
retire_age = input("At what age would you like to retire? ")

cur_age = int(cur_age)
retire_age = int(retire_age)
working_years = retire_age - cur_age

print("You have", working_years, "left until you can retire.")
print("It's ", year, ", so you can retire in ", year+working_years, ".", sep='')