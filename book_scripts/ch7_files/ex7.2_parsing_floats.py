"""
    Exercise 7.1

        Write a program to read through a file and print the contents of the
        file (line by line) all in upper case. Executing the program will look as follows:
        python shout.py
        Enter a file name: mbox-short.txt
        FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
        RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>

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
