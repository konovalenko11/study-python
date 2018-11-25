"""

    Exercise 10.1

        Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
        Count the number of messages from each person using a dictionary.

        After all the data has been read, print the person with the most commits by creating a list of (count, email)
        tuples from the dictionary. Then sort the list in reverse order and print out the person
        who has the most commits.

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


file_data = open("../assets/mbox.txt")
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

# get top N senders
print("\nTop list by value:")
print(get_top_dict_items_by_value_v1(email_count, 5))
print(get_top_dict_items_by_value_v2(email_count, 5))
