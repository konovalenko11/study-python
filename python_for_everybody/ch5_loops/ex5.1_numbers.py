"""
    Exercise 5.1

        Write a program which repeatedly reads numbers until the user enters “done”.
        Once “done” is entered, print out the total, count, and average of the numbers.
        If the user enters anything other than a number, detect their mistake using try and except and
        print an error message and skip to the next number.

    Enter a number: 4
    Enter a number: 5
    Enter a number: bad data
        Invalid input
    Enter a number: 7
    Enter a number: done
        16 3 5.33333333333

"""

numbers = []
numbers_cnt = 0
numbers_sum = 0

# parsing [score] value
while True:

    inStr = input("Please, enter number:\t")

    if inStr.lower() == "done":
        print("Input closed! Printing results.")
        break

    try:
        num = float(inStr)
        numbers.append(num)
        numbers_cnt += 1
        numbers_sum += num
    except ValueError as err:
        print("[ERROR] Please, enter numerical value.")
        print(err.args)


print("Numbers entered: %s; Total: [%.2f]; Count: [%d]; Avg: [%.2f]"
      % (numbers, numbers_sum, numbers_cnt, numbers_sum/numbers_cnt if numbers_cnt > 0 else 0))
