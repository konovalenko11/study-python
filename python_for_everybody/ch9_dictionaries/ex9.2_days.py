"""

    Exercise 9.2
    
        Write a program that categorizes each mail message by which day of the week the commit was done.
        To do this look for lines that start with “From”, then look for the third word and keep a running count of each
        of the days of the week. At the end of the program print out the contents of your dictionary
        (order does not matter).

"""

file_data = open("../assets/mbox-short.txt")
days_count = dict()

for line in file_data:

    if not line.startswith("From "):
        continue

    line_words = line.strip().split()
    print(line_words)

    if line_words[2]:
        days_count[line_words[2]] = days_count.get(line_words[2], 0) + 1

file_data.close()

print(days_count)