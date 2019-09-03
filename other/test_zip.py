####################################################
L1 = [3, 4, 5, 6]
L2 = [1, 2, 3, 7]
L4 = list(zip(L1, L2))
print(L4)
####################################################
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))

for (x1, x2) in L4:
    L3.append(x1+x2)

print(L3)
####################################################
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)
####################################################
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = list(map(lambda x: x[0] + x[1], zip(L1, L2)))
print(L3)
####################################################

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2  for (x1, x2) in zip(L1, L2) if x1 > 10 and x2 < 5]
print(L3)

####################################################
L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]

# maxs = map(lambda x: max(x), zip(L1, L2, L3))
maxs = [max(x) for x in zip(L1, L2, L3)]
####################################################
def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]

result2 = [x for s in L for x in s]
print(result2)
