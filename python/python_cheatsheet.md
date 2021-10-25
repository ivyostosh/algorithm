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