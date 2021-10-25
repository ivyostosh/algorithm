
# !!!Revisit - this example doesn't care about order
"""
https://leetcode.com/problems/binary-tree-paths/

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""

# Recursive approach
def binary_tree(self, root):
    def build_path(root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += '->'
                build_path(root.left, path)
                build_path(root.right, path)
    
    paths = []
    build_path(root, '')
    return paths


# Iterative approach
# Use a stack to store temporary paths
def binary_tree_iter(self, root):
    # edge case
    if not root:
        return []

    # Assign initial value
    paths = []
    stack = [(root, str(root.val))]

    while stack:
        # Pop a node and path from the stack every time
        node, path = stack.pop()
        # If we have reached a leaf node, we have found one complete path, append the path to paths
        if not node.left and not node.right:
            paths.append(path)
        # If we haven't reached a leaf node, we need to modify the path and add it back to the stack
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))
        if node.right:
            stack.append((node.right, path + '->' + str(node.right.val)))
    
    return paths
