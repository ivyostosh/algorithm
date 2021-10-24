"""
Binary Search Tree Traversal

- Use Cases:
    - Use non-recursion / iteration to perform BST inorder traversal
    - Can be used for more than BST

- Complexity:
    - Time: O(n)
    - Space: O(n)

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traversal(root):

    # Edge case
    if not root:
        return []

    # Create a dummy node with right child points to root
    
    dummy = TreeNode(0)
    dummy.right = root

    # Initialize variables
    stack = [dummy]
    inorder = []

    # Perform traversal
    while stack:
        node = stack.pop()
        # Append right, root, and all left children to the stack
        if node.right:
            node = node.right
            
            while node:
                stack.append(node)
                node = node.left
        
        # When poping from stack, the deepest left child will be poped first, then root, then right
        if stack:
            inorder.append(stack[-1])
        
    return inorder
