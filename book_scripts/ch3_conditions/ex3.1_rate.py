# Exercise 2.3 Write a program to prompt the user for hours and rate per hour to compute gross pay.
"""
    Exercise 2.3
        Write a program to prompt the user for hours and rate per hour to compute gross pay.

    Exercise 3.1

        Rewrite your pay computation to give the employee 1.5 times the
        hourly rate for hours worked above 40 hours.

        Enter Hours: 45
        Enter Rate: 10
        Pay: 475.0
"""

# parsing [hours] value
while True:
    try:
        hours = float(input("Please, indicate hours:\t"))
        break
    except ValueError:
        print("Please, enter hours in decimal/integer format.")

# parsing [rate] value
while True:
    try:
        rate = float(input("Please, indicate hour rate:\t"))
        break
    except ValueError:
        print("Please, enter hours rate in decimal/integer format.")

# checking on overtimes
if hours > 40:
    std_hours = 40
    overtime_hours = hours - std_hours
else:
    std_hours = hours
    overtime_hours = 0

payment = (std_hours * rate) + (overtime_hours * 1.5 * rate)

print("Total hours: [%.2f]; Overtime hours: [%.2f]; Rate: [$%.2f]; Total payment: [$%.2f]!"
      % (hours, overtime_hours, rate, payment));
