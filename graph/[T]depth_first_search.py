"""
Depth First Search

- Use Cases:
    - Find all options meeting certain conditions (99%)
    - Binary Tree (90%) (i.e Use non-recursion / iteration to perform BST inorder traversal)
    - Permutation (order matters) (95%)
    - Combination (order doesn't matter) (95%)

- Not Suited Use Cases:
    - Connected Components (use BFS to avoid stackoverflow)
    - Topological Sort (use BFS to avoid stackoverflow)
    - Anything that can be solved with BFS

- Complexity:
    - Time (O(time for one option * num of options)):
        Tree: O(n)
        Permutation: O(n! * n)
        Combination: O(2^N * n)


Key data structure: a stack.
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
