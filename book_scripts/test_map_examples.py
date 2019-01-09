####################################################
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = list(map(lambda x: x*2, lst))
print(greeting_doubled)
####################################################
# Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = list(filter(lambda x: 'w' in x, lst_check))
print(filter_testing)
####################################################