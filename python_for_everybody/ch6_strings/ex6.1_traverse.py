"""
    Exercise 6.1

        Write a while loop that starts at the last character in the string and
        works its way backwards to the first character in the string,
        printing each letter on a separate line, except backwards.

    Exercise 6.2

        Given that fruit is a string, what does fruit[:] mean?

"""

inStr = input("Please, enter string:\n")
i = len(inStr)
trStr = ""

while i >= 1:

    #    print("[%s]: [%s]" % (i, inStr[i-1]))
    trStr = trStr + inStr[i-1]

    i = i - 1

print("Traversed string: [%s]" % trStr)
print(inStr[::-1])
print(inStr.title())