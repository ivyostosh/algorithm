"""
Heap
- Use Cases:
    - Find max or min (60%)
    - Find k biggest item (if popping kth, O(nlogk)) (50%)
    - Require logn  time on the array (40%)

- Not Suited Use Cases:
    - Find closest number to a number (need balanced BST)
    - Find max / min on a range (segmentTree?)
    - O(n) to find k biggest item (Use partition in quick sort)

- Heap v.s. Sorted Array
                            Insert      Search      Find Min    Delete Min      Build
    Min Heap                O(logn)     O(n)        O(1)        O(logn)         O(n)
    Sorted Array            O(n)        O(logn)     O(1)        O(n)            O(nlogn)

"""

from heapq import heapify, heappush, heappop

# Python code to demonstrate working of 
# heapify(), heappush() and heappop()
  
# initializing list
li = [5, 7, 9, 1, 3]
print ("The initial list is : ",end="")
print(li)
  
# using heapify to convert list into heap
heapify(li)
  
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
  
# using heappush() to push elements into heap
# pushes 4
heappush(li, 4)
  
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))
  
# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heappop(li))

print ("The popped and smallest element is : ",end="")
print (heappop(li))