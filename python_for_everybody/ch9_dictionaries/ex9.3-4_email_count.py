"""

    Exercise 9.3

        Write a program to read through a mail log, build a histogram using a dictionary to count how many messages
        have come from each email address, and print the dictionary.

    Exercise 9.4

        Add code to the above program to figure out who has the most messages in the file.

"""

import collections as col


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


file_data = open("../assets/mbox-short.txt")
email_count = dict()

for line in file_data:

    if not line.startswith("From "):
        continue

    line_words = line.strip().split()
    print(line_words)

    if len(line_words) > 1:
        email_count[line_words[1]] = email_count.get(line_words[1], 0) + 1

file_data.close()

# full list
print("\nFull unsorted list, total elements[{}]:".format(len(email_count)))
print(email_count)

# get top 10 senders [option 1]
print("\nTop list by value:")
print(get_top_dict_items_by_value_v1(email_count, 3))
print(get_top_dict_items_by_value_v2(email_count, 3))
