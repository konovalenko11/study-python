"""
    Exercise 6.3

        Encapsulate this code in a function named count,
        and generalize it so that it accepts the string and the letter as arguments.

    Exercise 6.4

        There is a string method called count that is similar to the function in the previous exercise.
        Read the documentation of this method at https:// docs.python.org/2/library/stdtypes.html#string-methods and
        write an invocation that counts the number of times the letter a occurs in 'banana'.

    Exercise 6.5

        Take the following Python code that stores a string:‘

    str = 'X-DSPAM-Confidence: 0.8475'

"""


def char_count(data_string, find_char):
    char_matches: int = 0

    for char in data_string:
        if char == find_char:
            char_matches += 1

    return char_matches


#inStr = input("Please, enter string:\t")
#inChr = input("Please, enter char to find:\t")

#print(f"Input string: [{inStr}]; Find char: [{inChr}]; Matches1: [{char_count(inStr, inChr)}]; " +
#      f"Matches2: [{inStr.count(inChr)}]")

str = 'X-DSPAM-Confidence: 0.8475'
print("%.2f" % float(str[str.find(": ")+2:]))
