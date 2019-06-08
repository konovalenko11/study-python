#
# a = "felix"
#
# print(id(a))
#
# b = a
#
# print(id(b))
#
# c = "Felix"
#
# print(id(c))
#
# c = "felix"
#
# print(id(c))
##########################
# l1 = [1,2,3,4]
# l2 = [1,2,3,4]
# l3 = l1
# # l4 = l1[:]
# l4 = list(l1)
#
# print(id(l1))
# print(id(l2))
# print(id(l3))
# print(id(l4))
#
# l3[1] = 10
#
# print(l1)
# print(l2)
# print(l3)
# print(l4)
##########################
# l5 = "abc"
#
# l5.upper()
# print(id(l5))
# print(l5)
#
# l5 = l5.upper()
# print(id(l5))
# print(l5)
##########################
poplist = list("asdfghjkl")
print(poplist[5])

poplist.pop()
print(poplist)