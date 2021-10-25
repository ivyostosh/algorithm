"""
Dictionary in Python is a collection of data values, used to store data values like a map, which, 
unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. 
Key-value is provided in the dictionary to make it more optimized. 

Key requirement: have to appear only once, must be immutable (yes: int, float, string, boolean; no: list dict)

Important methods to remember:
Create: {}, {key: value}
Access: dict[key], dict.keys, key in dict.keys, dict.values(), dict.items()
Add / update: dict[key]
Delete: del dict[key], dict.pop(key), dict.popitem()   !!! Note pop for dict is different from list; the pop is based on key, not index
"""

########################################################################
print("===============Create a dictionary===============")

# Creating a Dictionary with Integer Keys
dict1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(dict1)

# Creating a Dictionary with Mixed keys
dict2 = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(dict2)

########################################################################
print("===============Access a dictionary===============")

# Return all keys using .keys()
print("\nDictionary with all keys: ")
print(dict1.keys())

# Check if a key exists using in .keys()
print("\nCheck if the Dictionary has a key 1: ")
print(1 in dict1.keys())
print("\nCheck if the Dictionary has a key 'test': ")
print("test" in dict1.keys())

# Return all values using .vales()
print("\nDictionary with all values: ")
print(dict1.values())

# Return all key, value tuple pairs using .items()
print("\nDictionary with all key, value pairs: ")
print(dict1.items())

# https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey
# .get(key, 'default value')

########################################################################
print("\n===============Add to a dictionary===============")

# Creating an empty Dictionary
dict3 = {}
print("Empty Dictionary: ")
print(dict3)
 
# Adding elements one at a time
dict3[0] = 'Geeks'
dict3[2] = 'For'
dict3[3] = 1
print("\nDictionary after adding 3 elements: ")
print(dict3)
 
# Adding set of values to a single Key
dict3['Value_set'] = 2, 3, 4
print("\nDictionary after adding set of values to a single key: ")
print(dict3)
 
# Updating existing Key's Value
dict3[2] = 'Welcome'
print("\nUpdated key value: ")
print(dict3)
 
# Adding Nested Key value to Dictionary
dict3[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(dict3)

########################################################################
print("\n===============Remove from a dictionary===============")

# Deleting a Key value using del
del dict3[5]
print("\nDeleting a specific key: ")
print(dict3)

# Delete and return the value of the key specified using pop()
# Deleting a key using pop() method
pop_ele = dict3.pop(2)  # Note this is not the index, but the key
print('\nDictionary after deletion: ' + str(dict3))
print('Value associated to poped key is: ' + str(pop_ele))

# Returns and removes an arbitrary element (key, value) pair using popitem()
# Deleting an arbitrary key
# using popitem() function
pop_ele = dict3.popitem()
print("\nDictionary after deletion: " + str(dict3))
print("The arbitrary pair returned is: " + str(pop_ele))


"""
How are dictionaries implemented in CPython? (https://docs.python.org/3/faq/design.html#how-are-dictionaries-implemented-in-cpython)

CPython’s dictionaries are implemented as resizable hash tables. 
Compared to B-trees, this gives better performance for lookup (the most common operation by far) under most circumstances, and the implementation is simpler.

Dictionaries work by computing a hash code for each key stored in the dictionary using the hash() built-in function. 
The hash code varies widely depending on the key and a per-process seed; for example, “Python” could hash to -539294296
while “python”, a string that differs by a single bit, could hash to 1142331976. 
The hash code is then used to calculate a location in an internal array where the value will be stored. 
Assuming that you’re storing keys that all have different hash values, this means that dictionaries take constant time – O(1), in Big-O notation – to retrieve a key.

"""

"""
Hash Table v.s. BST
https://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/
"""