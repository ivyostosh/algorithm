"""
https://www.geeksforgeeks.org/difference-between-recursion-and-iteration/

Recursion:
Used when code size needs to be small, and time complexity is not an issue.

Iteration
Used when time complexity needs to be balanced against an expanded code size.


Property	    Recursion	                                                                    Iteration
Definition	    Function calls itself.	                                                        A set of instructions repeatedly executed.
Application	    For functions.	                                                                For loops.
Termination	    Through base case, where there will be no function call.	                    When the termination condition for the iterator ceases to be satisfied.
Usage	        Used when code size needs to be small, and time complexity is not an issue.	    Used when time complexity needs to be balanced against an expanded code size.
Code Size	    Smaller code size	                                                            Larger Code Size.
Time Complexity	Very high(generally exponential) time complexity.	                            Relatively lower time complexity(generally polynomial-logarithmic).

"""


# https://stackoverflow.com/questions/235868/iterative-version-of-recursive-algorithm-to-make-a-binary-tree

"""
A recursive function with only one recursive call can usually be turned into a tail-recursive function without too much effort,
and then it's trivial to convert it into an iterative function. The canonical example here is factorial:
"""

# naïve recursion
def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)

# tail-recursive with accumulator
def fac(n):
    def fac_helper(n, k):
        if n <= 1:
            return k
        else:
            return fac_helper(n - 1, n * k)
    return fac_helper(n, 1)

# iterative with accumulator
def fac(n):
    k = 1
    while n > 1:
        n, k = n - 1, n * k
    return k

"""
However, your case here involves two recursive calls, and unless you significantly rework your algorithm, you need to keep a stack. 
Managing your own stack may be a little faster than using Python's function call stack, but the added speed and depth will probably not be worth the complexity. 
The canonical example here would be the Fibonacci sequence:
"""

# naïve recursion
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# tail-recursive with accumulator and stack
def fib(n):
    def fib_helper(m, k, stack):
        if m <= 1:
            if stack:
                m = stack.pop()
                return fib_helper(m, k + 1, stack)
            else:
                return k + 1
        else:
            stack.append(m - 2)
            return fib_helper(m - 1, k, stack)
    return fib_helper(n, 0, [])

# iterative with accumulator and stack
def fib(n):
    k, stack = 0, []
    while 1:
        if n <= 1:
            k = k + 1
            if stack:
                n = stack.pop()
            else:
                break
        else:
            stack.append(n - 2)
            n = n - 1
    return k