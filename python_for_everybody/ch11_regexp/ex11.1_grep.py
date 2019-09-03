"""

    Exercise 11.1

        Write a simple program to simulate the operation of the grep command on Unix.
        Ask the user to enter a regular expression and count the number of lines that matched the regular expression

"""

import re


def get_input_str():
    while True:
        try:
            input_str = input("Please, enter regExp pattern:\t")

            if len(input_str) == 0:
                raise ValueError()
            break
        except ValueError:
            print("Input is empty. Please try once more!")

    return input_str


file_data = open("../assets/mbox.txt")

input_pattern = get_input_str()
pattern = re.compile(input_pattern)

i = 0
for line in file_data:

    if re.search(pattern, line):
        i += 1
        print(line.strip())

file_data.close()

print(f"For pattern [{input_pattern}] were found [{i}] matches")