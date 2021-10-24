# LinkedList Implementation (https://www.educative.io/blog/8-python-data-structures

# Define node
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    
class SLinkedList:
    def __init__(self):
        self.headval = None

# Initiate the SLinkedList
list1 = SLinkedList()

# Define nodes
e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Assign head
list1.headval = e1

# Link nodes
e1.nextval = e2
e2.nextval = e3

# Traverse through the SLinkedList
head = list1.headval
while head:
    print(head.dataval)
    head = head.nextval

########################################################################
# Common linked list interview questions in Python
"""
Print the middle element of a given linked list
Remove duplicate elements from a sorted linked list
Check if a singly linked list is a palindrome
Merge K sorted linked lists
Find the intersection point of two linked lists
"""

########################################################################
# Common circular linked list interview questions in Python
"""
Detect loop in a linked lists
Reverse a circular linked list
Reverse circular linked list in groups of give size
"""
