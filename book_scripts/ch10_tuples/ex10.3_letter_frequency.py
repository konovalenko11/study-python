"""

    Exercise 10.3

        Write a program that reads a file and prints the letters in decreasing order of frequency.
        Your program should convert all the input to lower case and only count the letters a-z.
        Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
        Find text samples from several different languages and see how letter frequency varies between languages.
        Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

"""

import collections as col
import re


def get_top_dict_items_by_value_v1(d, top=0):
    if len(d) < top or top == 0:
        return sorted(d.items(), key=lambda x: x[1], reverse=True)[:len(d)]
    else:
        return sorted(d.items(), key=lambda x: x[1], reverse=True)[:top]


def get_top_dict_items_by_value_v2(d, top=0):

    r = col.Counter(d)

    if top == 0:
        return r.most_common()
    else:
        return r.most_common(top)


file_data = open("../assets/mbox.txt")

line_cleaned = ""
i = 0
letters = dict()

for line in file_data:

    line_cleaned = re.sub(r"[^a-z]", "", line.strip().lower())

    for letter in line_cleaned:
        letters[letter] = letters.get(letter, 0) + 1

for letter, frequency in get_top_dict_items_by_value_v1(letters):
    print(f"Letter [{letter}]: [{frequency}];")

file_data.close()
