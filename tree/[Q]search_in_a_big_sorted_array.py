"""
Given a big sorted array with positive integers sorted by ascending order. 
The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). 
Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.
"""

# Implement find bounds for binary search
def find_pos(arr, target):
    
    # Assign initial value
    low = 0
    high = 1
    val = arr[0]

    # Increment low and high to find a lower bound and upper bound for target
    while val < target:
        low = high
        high = high * 2
        val = arr[high] # No need to check out of bound error since the assumption is this is a "big" array
    
    return binary_search(arr, target, low, high)


# Implement binary search

def binary_search(arr, target, low, high):
    
    while (low <= high):
        mid = (low + high) // 2

        # arr[mid] equals target
        if arr[mid] == target:
            return mid

        # arr[mid] less than target, update low
        elif arr[mid] < target:
            low = mid + 1

        # arr[mid] greater than target, update high
        else:
            high = mid - 1
    
    # If the value is not present, return
    return -1

# Driver function
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = find_pos(arr, 10)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)