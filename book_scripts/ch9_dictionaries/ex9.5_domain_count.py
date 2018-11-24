"""

    Exercise 9.5

        This program records the domain name (instead of the address) where the message was sent from
        instead of who the mail came from (i.e., the whole email address).
        At the end of the program, print out the contents of your dictionary.

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


file_data = open("../assets/mbox-short.txt")
domain_count = dict()

for line in file_data:

    # check if line contains info we need
    if not line.startswith("From "):
        continue

    line_words = line.strip().split()
    print(line_words)

    # check if line contains data we need
    if len(line_words) < 2 or len(re.split("@", line_words[1])) < 2:
        continue

    email_items = re.split("@", line_words[1])
    domain_count[email_items[1]] = domain_count.get(email_items[1], 0) + 1

file_data.close()

# full list
print("\nFull unsorted list, total elements[{}]:".format(len(domain_count)))
print(domain_count)

# get top 10 senders [option 1]
print("\nTop list by value:")
print(get_top_dict_items_by_value_v1(domain_count, 3))
print(get_top_dict_items_by_value_v2(domain_count, 3))
