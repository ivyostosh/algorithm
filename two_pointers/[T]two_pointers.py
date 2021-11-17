"""
Two pointers

- Use Cases:
    - Sliding window (90%)
    - Time complexity requires O(n) (80%)
    - Require in place update; can only use swap, no extra space (80%)
    - have keywords subarray / substring (50%)
    - have keywords palindrome (50%)

- Complexity:
    - Time: O(n) - depended on the number of executions on the most inner loop, not the number of loops.
    - Space: O(1) - just need two points

"""

# 相向pointers (patition in quicksort)
def patition(self, A, start, end):
    if start >= end:
        return

    left, right = start, end

    # [Tip1] pivot is for the value, not the index
    pivot = A[(start + end) // 2]

    # [Tip2] every time comparing left & right, it should be left <= right, not left < right
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        
        while left <= right and A[right] > pivot:
            right -= 1
        
        if left <= right:
            A[left], A[right] = A[right], A[left]

            left += 1
            right -= 1

# 背向pointers
def reverse_pointers(self, A, position):
    left = position
    right = position + 1

    while left >= 0 and right < len(A):
        # if left and right can stop:
            # break
        
        left -= 1
        right += 1

# Same direction pointers
def same_direction_pointers(self, n, position):
    j = 0

    for i in range(n):
        # while j < n and i and j doesn't meet condition:
            # j += 1
        
        # if i and j meets conditions:
        #     handle the window between i and j

        # judt to avoid error
        pass
    
# Merge with two pointers
def merge(self, list1, list2):
    new_list = []
    i, j = 0, 0

    # During merge, we can only update i, j.
    # list1.pop(0) and similar actions are not allowed since pop(0) requires O(n)
    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    # Merge the remaining items to the new list
    # new_list.extend(list1[i:]) and similar actions are not allowed since slicing requires additional space
    while i < len(list1):
        new_list.append(list1[i])
        i += 1

    while j < len(list2):
        new_list.append(list2[j])
        j += 1
    
    return new_list
    
    
    





