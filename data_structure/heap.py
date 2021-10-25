"""
Heap
- Use Cases:
    - Find max or min (60%)
    - Find k biggest item (if popping kth, O(nlogk)) (50%)
    - Require logn time on the array (40%)

- Not Suited Use Cases:
    - Find closest number to a number (need balanced BST)
    - Find max / min on a range (segmentTree?)
    - O(n) to find k biggest item (Use partition in quick sort)

- Heap v.s. Sorted Array (https://www.geeksforgeeks.org/difference-between-heaps-and-sorted-array/)
                            Insert      Search      Find Min    Delete Min      Build
    Min Heap                O(logn)     O(n)        O(1)        O(logn)         O(n)
    Sorted Array            O(n)        O(logn)     O(1)        O(n)            O(nlogn)

# If maxheap, use minheap, but negate the values.

"""

from heapq import heapify, heappush, heappop

# Python code to demonstrate working of 
# heapify(), heappush() and heappop()
  
# initializing list
li = [5, 7, 9, 1, 3]
# if the list contains tuples, the first element will be used to determine the priority in the heap
li2 = [(5, "a"), (7, "b"), (9, "c"), (1, "d"), (3, "e")]
print("The initial list is : ",end="")
print(li)
print("The initial list2 is : ",end="")
print(li2)

# using heapify to convert list into heap
heapify(li)
heapify(li2)
  
# printing created heap
print("The created heap is : ",end="")
print(list(li))
print("The created heap2 is : ",end="")
print(list(li2))
  
# using heappush() to push elements into heap
# pushes 4
heappush(li, 4)
# Pushs (4, "f")
heappush(li2, (4, "f"))
  
# printing modified heap
print("The modified heap after push is : ",end="")
print(list(li))
print("The modified heap2 after push is : ",end="")
print(list(li2))
  
# using heappop() to pop smallest element
print("The popped and smallest element for heap is : ",end="")
print(heappop(li))
print("The popped and smallest element for heap2 is : ",end="")
print(heappop(li2))

"""
https://favtutor.com/blogs/heap-in-python
"""