# sorted()
sorted() can take a maximum of three parameters:

iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

We can also use [::,-1] to achieve the same reversal function.

# random
import random

random.shuffle(x[, random])
Shuffle the sequence x in place.
The optional argument random is a 0-argument function returning a random float in [0.0, 1.0); by default, this is the function random().

random.random()
Return the next random floating point number in the range [0.0, 1.0).

random.choice(seq)
Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.


# Error catching
Try to be specific of the error (https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

try:
    raise ValueError('xxxxx')
except ValueError:
    print('There was an exception.')

# Collection


# String
' '.join()

Split string to substrings by delimiter
list.split("delimiter")

Split string to character
list(str)


# int with different bases
https://stackoverflow.com/questions/23190060/what-does-base-value-do-in-int-function

It does exactly what it says - converts a string to integer in a given numeric base. As per the documentation, int() can convert strings in any base from 2 up to 36. On the low end, base 2 is the lowest useful system; base 1 would only have "0" as a symbol, which is pretty useless for counting. On the high end, 36 is chosen arbitrarily because we use symbols from "0123456789abcdefghijklmnopqrstuvwxyz" (10 digits + 26 characters) - you could continue with more symbols, but it is not really clear what to use after z.

"Normal" math is base-10 (uses symbols "0123456789"):

int("123", 10)  # == 1*(10**2) + 2*(10**1) + 3*(10**0) == 123
Binary is base-2 (uses symbols "01"):

int("101", 2)   # == 1*(2**2) + 0*(2**1) + 1*(2**0) == 5
"3" makes no sense in base 2; it only uses symbols "0" and "1", "3" is an invalid symbol (it's kind of like trying to book an appointment for the 34th of January).

int("333", 4)   # == 3*(4**2) + 3*(4**1) + 3*(4**0)
                # == 3*16 + 3*4 + 3*1
                # == 48 + 12 + 3
                # == 63


# divmid
The divmod() method in python takes two numbers and returns a pair of numbers consisting of their quotient and remainder. 
Input : x = 9, y = 3
Output :(3, 0)

Input : x = 8, y = 3
Output :(2, 2)

# find
If find() doesn't find a match, it returns -1, otherwise it returns the left-most index of the substring in the larger string.
fullstring = "StackAbuse"
substring = "tack"

if fullstring.find(substring) != -1:
    print("Found!")
else:
    print("Not found!")

# isalnum()
The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.


# reverse v.s. reversed v.s. slicing

foo.reverse() actually reverses the elements in the container.
reversed() doesn't actually reverse anything, it merely returns an object that can be used to iterate over the container's elements in reverse order. -> As the return value is an object, in order to directly use it, you need to do list(xx) to convert it to a list.


# enumerate()
enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.

enumerate(iterable, start=0)

Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is 
              to be started, by default it is 0

# count()
list.count(target)
str.count(target, start, end)

# zip()
for w, v in zip(words1, words2)
good use case when we are iterating two same length lists with the SAME indexes. 


# Pass by reference
https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference


# check type

type(object)

To check if o is an instance of str or any subclass of str, use isinstance (this would be the "canonical" way):

if isinstance(o, str):
To check if the type of o is exactly str (exclude subclasses):

if type(o) is str:
The following also works, and can be useful in some cases:

if issubclass(type(o), str):


# Create 2D array
list = [[False for _ in range(len(matrix[0])] for _ in range(len(matrix))]


# zip(*)
https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist/29139418