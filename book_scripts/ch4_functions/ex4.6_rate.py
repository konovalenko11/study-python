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

    Exercise 4.6

        Rewrite your pay computation with time-and-a-half for overtime and create a function called
        computepay which takes two parameters (hours and rate).

"""


def computepay(fhours, frate, fplanned_hours=40, fovertime_rate_coef=1.5):
    overtime_hours = max(fhours - fplanned_hours, 0)
    regular_hours = fhours - overtime_hours

    return dict(
        payment=(regular_hours * frate) + (overtime_hours * frate * fovertime_rate_coef),
        regular_hours=regular_hours,
        overtime_hours=overtime_hours,
        planned_hours=fplanned_hours,
        overtime_rate_coef=fovertime_rate_coef
    )


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
payment = computepay(hours, rate)

print("Total hours: [%.2f]; Overtime hours: [%.2f]; Rate: [$%.2f]; Total payment: [$%.2f]!"
      % (hours, payment['overtime_hours'], rate, payment['payment']));
