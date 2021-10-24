"""
Binary Tree Divide & Conquer

- Use Cases:
    - Binary tree related questions (99%)
    - A problem that can be splitted into half and merged afterwards to get the result (100%)
    - Array related problems (10%)

- Complexity:
    - Time: O(n)
    - Space: O(n) - including the stack for recursion

"""

def divide_conquer(root):
    # Exit case
    if not root:
        return # something
    
    # Handle left part
    left_result = divide_conquer(root.left)

    # Handle right part
    right_result = divide_conquer(root.right)

    # Merge results
    result = None # merge left_result and right_result

    return result