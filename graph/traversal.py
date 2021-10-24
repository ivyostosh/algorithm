"""
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
Depth First Traversals: 
(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
Breadth First or Level Order Traversal : 1 2 3 4 5
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def printInorder(root):
    """
    In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order.
    To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal s reversed can be used. 
    """

    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPreorder(root):
    """
    Preorder traversal is used to create a copy of the tree.
    Preorder traversal is also used to get prefix expression on of an expression tree.
    Please see http://en.wikipedia.org/wiki/Polish_notation to know why prefix expressions are useful. 
    """

    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
    
def printPostorder(root):
    """
    Postorder traversal is used to delete the tree. Please see the question for deletion of tree for details.
    Postorder traversal is also useful to get the postfix expression of an expression tree.
    Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for the usage of postfix expression.
    """

    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)
 
print("\nInorder traversal of binary tree is")
printInorder(root)
 
print("\nPostorder traversal of binary tree is")
printPostorder(root)