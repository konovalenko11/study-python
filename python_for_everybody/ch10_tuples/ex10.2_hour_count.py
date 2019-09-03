"""

    Exercise 10.2

        This program counts the distribution of the hour of the day for each of the messages.
        You can pull the hour from the “From” line by finding the time string and then splitting that string into parts
        using the colon character. Once you have accumulated the counts for each hour, print out the counts,
        one per line, sorted by hour as shown below.

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
hour_count = dict()

for line in file_data:

    if not line.startswith("From "):
        continue

    line_words = line.strip().split()
    print(line_words)

    if len(line_words) <= 5:
        continue

    # defining pattern to parse date in 6th word of the line [HH24:mm:ss]
    datetm_pattern = re.compile(r"\d\d:\d\d:\d\d")
    datetm = line_words[5]

    if re.match(datetm_pattern, datetm):
        hour = re.split(":", datetm)[0]
    else:
        hour = "-1"

    hour_count[hour] = hour_count.get(hour, 0) + 1

    print("Datetime: [{}]; Hour: [{}].".format(datetm, hour))

file_data.close()

# full list
print("\nFull unsorted list, total elements[{}]:".format(len(hour_count)))
print(hour_count)

# get top N senders
print("\nTop list by value:")
print(get_top_dict_items_by_value_v1(hour_count, 5))
print(get_top_dict_items_by_value_v2(hour_count, 5))
