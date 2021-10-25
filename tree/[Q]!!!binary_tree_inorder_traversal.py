"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

https://www.jiuzhang.com/solutions/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

"""

# Recursive Approach

def inorder_traversal(self, root):

    def inorder_traversal_helper(root):
        # Exit case
        if not root:
            return

        # Recursive cases
        if root.left:
            inorder_traversal(root.left)
        paths.append(root.val)

        if root.right:
            inorder_traversal(root.right)
    
    paths = []
    inorder_traversal_helper(root)

    return paths


# Iterative Approach

def inorder_traversal(self, root):

    # Edge case
    if not root:
        return []

    # Assing initial values
    stack = []
    paths = []
    node = root

    # Load to the stack, pop and append to paths in the order of left, root, then right. Repeat.
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        paths.append(node.val)

        node = node.right
    
    return paths


