"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

"""

def find_min(arr):

    # Assign initial value
    low = 0
    high = len(arr) - 1

    # Iteratively find the target
    while low <= high:
        mid = (low + high) // 2
        
        # Exit condition
        if mid == 0:
            return min(arr[0], arr[-1])
        
        elif arr[mid] < arr[mid - 1]:
            return arr[mid]

        # If the target is greater than the first element, take the right half and re-run
        elif arr[mid] > arr[0]:
            low = mid + 1

        # if the target is less than the first element, take the left half and re-run
        # Note to not plus 1 here
        else:
            high = mid
    
    return arr[0]

    
arr = [4,5,6,7,0,1,2]
res = find_min(arr)
print(res)



