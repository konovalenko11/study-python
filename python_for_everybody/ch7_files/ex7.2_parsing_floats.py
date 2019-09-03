"""
    Exercise 7.2

        Write a program to prompt for a file name, and then read through the file and look for lines of the form:
            X-DSPAM-Confidence: 0.8475
        When you encounter a line that starts with “X-DSPAM-Confidence:”
        pull apart the line to extract the floating-point number on the line.
        Count these lines and then compute the total of the spam confidence values from these lines.
        When you reach the end of the file, print out the average spam confidence.

        Enter the file name: mbox.txt
        Average spam confidence: 0.894128046745

        Enter the file name: mbox-short.txt
        Average spam confidence: 0.750718518519

"""

file = open("mbox-short.txt")
search_str = "X-DSPAM-Confidence: "
value_sum = 0
value_cnt = 0

for line in file:
    if line.startswith(search_str):

        try:
            value = float(line[line.find(": ") + 2:])
        except ValueError:
            continue

        print("Line: [%s]; Value: [%f]" % (line.rstrip(), value))

        value_sum += value
        value_cnt += 1

print("Total values: [{}]; Sum: [{:.4f}]; Avg: [{:.4f}].".format(
    value_cnt, value_sum, 0 if value_cnt == 0 else value_sum / value_cnt))

file.close()
