"""
    Exercise 5.2

        Write another program that prompts for a list of numbers as above and at the end prints out both
        the maximum and minimum of the numbers instead of the average.

    Enter a number: 4
    Enter a number: 5
    Enter a number: bad data
        Invalid input
    Enter a number: 7
    Enter a number: done

"""

numbers = []
numbers_cnt = 0
numbers_sum = 0
numbers_min = 0
numbers_max = 0

# parsing [score] value
while True:

    inStr = input("Please, enter number:\t")

    if inStr.lower() == "done":
        print("Input closed! Printing results.")
        break

    try:
        num = float(inStr)
    except ValueError as err:
        print("[ERROR] Please, enter numerical value.")
        print(err.args)
        continue

    numbers.append(num)
    numbers_cnt += 1
    numbers_sum += num
    numbers_min = num if num < numbers_min else numbers_min
    numbers_max = num if num > numbers_max else numbers_max

print("Numbers entered: %s; Total: [%.2f]; Count: [%d]; Min: [%.2f]; Max: [%.2f]"
      % (numbers, numbers_sum, numbers_cnt, numbers_min, numbers_max))
