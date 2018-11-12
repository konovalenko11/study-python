"""
    Exercise 2.5

    Write a program which prompts the user for a Celsius temperature,
    convert the temperature to Fahrenheit, and print out the converted temperature.
"""

celsius_temp = int(input("Please, enter temperature in Celsius:\t"))
fahrenheit_temp = (celsius_temp * 9 / 5) + 32

print("Temperature in Fahrenheits is: [%s]" % fahrenheit_temp)


