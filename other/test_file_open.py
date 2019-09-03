fname = "assets/mbox-short.txt"

with open(fname, 'r') as fileref:         # step 1
    for line in fileref:
        print(line)
