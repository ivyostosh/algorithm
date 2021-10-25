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

    # Initialize variables
    stack = []
    inorder = []
    node = root

    # Perform traversal
    while node or stack:
        
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        inorder.append(node.val)

        node = node.right
        
    return inorder
