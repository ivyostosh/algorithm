"""
Binary Search 

- Use Cases:
    - Find a split position in a array such that the left meets certain condition while the right doesn't (100%)
    - Find an algorithm better than O(n) (99%)
    - Find a max / min value such that a certain condition can be satisfied (90%)
    - Sort an array (30 - 40%)

- Complexity:
    - Time: O(logn)
    - Space: O(1)

"""

# Template

def binary_search(self, nums, target):

    # Edge case
    if not nums:
        return -1

    # Assign initial values
    start = 0
    end = len(nums) - 1

    # Iterate from start to end, use + 1 to avoid infinite loops
    # [Tip1] use start + 1 < end
    while start + 1 < end:

        # [Tip2] use // 2 for python. (use start + (end - start) / 2 for C++ and Java)
        mid = (start + end) // 2

        # [Tip3] Separately discuss =, < and >, don't use + 1 or - 1 for mid
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            start = mid

        else:
            end = mid
    
    # Return results
    # As we used start + 1 and end as the comparison above, the target can be at either start or end

    # [Tip4] Handle start and end separately after the while loop
    if nums[start] == target:
        return start
    
    if nums[end] == target:
        return end

    return -1


# (https://www.geeksforgeeks.org/python-program-for-binary-search/)

# Recursive Approach

def binary_search_rec(arr, x, low, high):

    # Exit case
    # If the element doesn't exist in the array, return -1
    if low > high:
        return -1

    # Regular cases
    mid = (low + high) // 2

    # If the mid happens to the x, return mid
    if arr[mid] == x:
        return mid
    
    # If the mid is smaller than x, run binary search on the right half of the array
    if arr[mid] < x:
        return binary_search_rec(arr, x, mid + 1, high)
    
    # If the mid is grater than x, run binary search on the right half of the array
    else:
        return binary_search_rec(arr, x, low, mid - 1)
    
# Iterative Approach

def binary_search_iter(arr, x):

    # Assign initial values
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        # If the mid happens to the x, return mid
        if arr[mid] == x:
            return mid
        
        # If the mid is smaller than x, update low
        elif arr[mid] < x:
            low = mid + 1

        # If the mid is grater than x, update high
        else:
            high = mid - 1
    
    # If cannot find the value return
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10
 
print("Function call for resursive approach")
result = binary_search_rec(arr, x, 0, len(arr)-1)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

print("\nFunction call for iterative approach")

result = binary_search_iter(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")