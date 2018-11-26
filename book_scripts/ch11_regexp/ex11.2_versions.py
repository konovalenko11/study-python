"""

    Exercise 11.2

        Write a program to look for lines of the form

        New Revision: 39772

        and extract the number from each of the lines using a regular expression and the findall() method.
        Compute the average of the numbers and print out the average.

"""

import re

file_data = open("../assets/mbox.txt")

input_pattern = "New Revision:\s(\d+)"
pattern = re.compile(input_pattern)

i = 0
sum = 0

for line in file_data:

    rev_number_expr = re.search(pattern, line.strip())

    if rev_number_expr:
        i += 1
        sum += int(rev_number_expr.group(1))
        print(line.strip() + "; Revision: " + rev_number_expr.group(1))
    else:
        continue

if i > 0:
    avg = sum/i
else:
    avg = 0

file_data.close()

print(f"Number of items found: [{i}]; Sum: [{sum}]; Avg: [{avg}]")