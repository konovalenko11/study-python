# Exercise 2.3 Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = float(input("Please, indicate hours:\t"))
rate = float(input("Please, indicate rate per hour $: \t"))

payment = hours * rate

print("For [%f] hours and [$ %f] rate you will have [$ %f] money!" % (hours, rate, payment));
