# test = []

# if test:
#     print("Empty list is true")
# else:
#     print("Empty list is false")

# ??? need to research
# test_append = [1, 2, 3, 4]
# test_append.append([])
# print(test_append)


# list1 = [1, 1, 2]
# set1 = set(list1)
# print(set1)


from collections import Counter
list = [2,4,1,8,2,4]
dict = Counter(list)
print(dict)
dict.subtract([1,2])
print(dict)
