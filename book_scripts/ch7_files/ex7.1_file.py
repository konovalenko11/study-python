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

for line in file:
    if line.startswith("From:"):
        print(line.rstrip().upper())
