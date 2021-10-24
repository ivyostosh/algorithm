# Queue Implementation (https://www.educative.io/blog/8-python-data-structures

"""
We can use append() and pop() to implement a queue, but this is inefficient as lists must shift elements one by one.
Instead, the best practice is to use a deque from collections module.
Deques (double-ended queue) allow you to access both sides of the queue through popleft() and popright()

Important methods to remember:
queue.append(), queue.appendleft(),
queue.pop(), queue.popleft()
"""

########################################################################
print("===============Create a deque===============")

from collections import deque

# Initialize a deque
# Option 1: Empty deque
q = deque()
# Option 2: deque with values
q = deque(['a', 'b', 'c'])
print(q)

########################################################################
print("\n===============Add to a deque===============")

# Add element to the right end of deque: using append()
q.append('d')
q.append('e')
q.append('f')
print("\nAdd to a queue using append()")
print(q)

# Add element to the left end of deque: using appendleft()
q.appendleft(1)
q.appendleft(2)
print("\nAdd to a queue using appendleft()")
print(q)

print("\nNote deque can hold different types of elememt as shown above")

########################################################################
print("\n===============Delete from a deque===============")

# Delete element from the right end of deque: using pop()
q.pop()
q.pop()
print("\nDelete from the right end of the queue using pop()")
print(q)

# Delete element from the left end of deque: using popleft()
q.popleft()
print("\nDelete from the left end of the queue using popleft()")
print(q)

########################################################################
# Common queue interview questions in Python

"""
Reverse first k elements of a queue
Implement a queue using a linked list
Implement a stack using a queue
"""