"""
Simple Array Manipulation (https://www.educative.io/blog/8-python-data-structures

Important methods to remember:
len(list), 
list.append(), list.insert(index, value),
list.pop(), list.pop(index), del list[index:index], list.remove(value)
"""

########################################################################
print("===============Create a list===============")

fruits = ["apple", "banana", "orange", "mango"]
fruits2 = ["blueberry", "strawberry"]
fruits3 = ["kiwi", "Dragonfruit"]
print("Fruit List:")
print(fruits)

########################################################################
print("\n===============Get size of a list===============")

# using len()
print("Fruit List Size:")
print(len(fruits))

########################################################################
print("\n===============Append to a list===============")

# Append to the end of the list: using append()
print("Add a fruit at the end of the list:")
fruits.append("watermelon")
print(fruits)

# Append to the beginning or middle the list: using insert()
print("\nAdd a fruit at the beginning / middle of the list:")
fruits.insert(1, "watermelon")
print(fruits)

########################################################################
print("\n===============Delete from a list===============")

# delete from the right side: using pop()
print("\nDelete a fruit from the end of the list:")
fruits.pop()
print(fruits)

# delete with an index: using pop(n)
print("\nDelete a fruit using index:")
fruits_pop = fruits.pop(0)
print(fruits)

# delete with an index: using del
print("\nDelete a fruit using del:")
del fruits[0:2]
print(fruits)

# Difference comparison
print("\nPop returns the deleted value, while del doesn't")
print(fruits_pop)

# delete with value: using remove
print("\nRemove a value using remove:")
fruits.remove('mango')
print(fruits)

# delete all: using clear
print("\nRemove all values using clear:")
fruits.clear()
print(fruits)

########################################################################
print("\n===============Combine two lists===============")

## Comparison: extend update the origial list, + doesn't

# Using extend()
print("\nCombine Fruits2:")
fruits.extend(fruits2)
print(fruits)

# Using + operator
print("\nCombine Fruits3:")
fruits = fruits + fruits3
print(fruits)

########################################################################
print("\n===============Loop through two lists===============")

print("\nIterate through the Fruits list:")
for x in fruits:
    print(x)

########################################################################
# Common arrays interview questions in Python
"""
Remove even integers from list
Merge two sorted lists
Find minimum value in a list
Maximum sum sublist
Print products of all elements
"""