"""
# https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

# !!!: how do we access the matrix

def binary_search(matrix, target):
    # Assess dimension and handle edge case
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    # Assign initial values for left and right pointers
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        # !!!: be aware we are using n for both dimensions
        mid_elem = matrix[mid // n][mid % n]

        # exit case, find the target
        if  mid_elem == target:
            return True

        # if the mid is smaller than the target, update low
        elif mid_elem < target:
            left = mid + 1

        # if the mid is grater than the target, update high
        else:
            right = mid - 1
        
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
res = binary_search(matrix, target)
print(res)


