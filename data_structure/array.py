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

"""
Common arrays interview questions in Python

Remove even integers from list
Merge two sorted lists
Find minimum value in a list
Maximum sum sublist
Print products of all elements
"""


"""
How are lists implemented in CPython? (https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython)

CPython’s lists are really variable-length arrays, not Lisp-style linked lists. 
The implementation uses a contiguous array of references to other objects, and keeps a pointer to this array and the array’s length in a list head structure.
This makes indexing a list a[i] an operation whose cost is independent of the size of the list or the value of the index.
When items are appended or inserted, the array of references is resized. 
Some cleverness is applied to improve the performance of appending items repeatedly; 
when the array must be grown, some extra space is allocated so the next few times don’t require an actual resize.
"""