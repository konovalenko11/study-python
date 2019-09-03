"""
    Exercise 8.6

        Rewrite the program that prompts the user for a list of numbers and prints out the maximum and
        minimum of the numbers at the end when the user enters “done”.

        Write the program to store the numbers the user enters in a list and use the max() and min() functions
        to compute the maximum and minimum numbers after the loop completes.

"""

numbers = []

while True:

    inStr = input("Please, enter number:\t")

    if inStr.lower() == "done":
        print("Input closed! Printing results.")
        break

    try:
        num = float(inStr)
        numbers.append(num)
    except ValueError as err:
        print("[ERROR] Please, enter numerical value.")
        print(err.args)


print("Numbers entered: %s; Total: [%.2f]; Count: [%d]; Min: [%.2f]; Max: [%.2f]"
      % (numbers, sum(numbers), len(numbers), min(numbers), max(numbers)))
