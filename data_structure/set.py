"""
Set (https://www.geeksforgeeks.org/python-set-methods/)
Very important: set is unordered and mutable. 
You cannot specify deleting an element from set by index since it's unordered, but you can delete by element using remove().

Important methods to remember:
{'value'} or set(),
set.add(),
set.remove('value'), set.pop() -> this pops a RANDOM element!
"""

########################################################################
print("===============Create a set===============")

fruits = {"apple", "banana", "orange", "mango"}
fruits2 = {}
fruits3 = set()
print("Create a set")
print(fruits)

print("\nNote if you initialize the set using {}, this will be a dictionary, not a set.")
print("fruits is a {}, fruits2 is a {}".format(type(fruits), type(fruits2)))
print("\nUse set() instead to create empty set")
print("fruits3 is a {}".format(type(fruits3)))

########################################################################
print("\n===============Add to a set===============")

# Use add()
fruits.add("Kiwi")
print(fruits)

########################################################################
print("\n===============Remove from a set===============")

# pop(): Returns and removes a random element from the set
# Emphasize on the random!!!
deleted_fruit = fruits.pop()

print("Delete from a set")
print(fruits)
print("\nThe removed fruit is")
print(deleted_fruit)

# remove(): Removes the element from the set
fruits.remove("Kiwi")
print("Delete from a set")
print(fruits)