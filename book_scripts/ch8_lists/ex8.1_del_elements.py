"""

    Exercise 8.1
    
    Write a function called chop that takes a list and modifies it, 
    removing the first and last elements, and returns None.

    Then write a function called middle that takes a list and 
    returns a new list that contains all but the first and last elements.

"""


def chop(test_list):
    if test_list:
        print('deleting...')
        del test_list[0]

    if test_list:
        print('deleting...')
        del test_list[-1]


def middle(test_list):
    if len(test_list) > 0:
        print('working...')
        return test_list[1:-1]
    else:
        return []


t = [1, 3, 5, 6, 7, 3, 56, 7]
m = [1, 2]
e = []

chop(t)
print(t)

chop(m)
print(m)

chop(e)

t = [1, 3, 5, 6, 7, 3, 56, 7]
m = [1, 2]
e = []

print(middle(t))
print(middle(m))
print(middle(e))


