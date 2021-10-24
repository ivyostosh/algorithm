# !!!: need to re-do the process, not too comfortable with the entire write-up
"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Divide and conquer
def max_depth(root):
    # Exit case
    if not root:
        return 0
    
    # Regular cases
    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1

