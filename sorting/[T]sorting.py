"""
Sorting

- Complexity:
    Quick Sort
    - Time: best O(nlogn), average O(nlogn), worst O(n^2)
    - Space: O(1)
    Merge Sort
    - Time: best O(nlogn), average O(nlogn), worst O(nlogn)
    - Space: O(n)

"""


# Quick Sort

class Solution:
    def sortInteger(self, A):
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
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
            
            if left <= right:   # Indicate left greater than the right
                A[left], A[right] = A[right], A[left]

                left += 1
                right -= 1
            
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


# Merge Sort

class Solution:
    def sortIntegers(self, A):
        if not A:
            return A
        temp = [0] * len(A)
        self.mergeSort(A, 0, len(A)-1, temp)

    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return

        # Sort left half
        self.mergeSort(A, start, (start + end) // 2, temp)

        # Sort right half
        self.mergeSort(A, (start + end) // 2, end, temp)

        # Merge two halves
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):
        mid = (start + end) // 2
        left = start
        right = mid + 1
        index = start

        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                index += 1
                left += 1
            else:
                temp[index] = A[right]
                index += 1
                right += 1
        
        while left <= mid:
            temp[index] = A[left]
            index += 1
            left += 1
        
        while right <= end:
            temp[index] = A[right]
            index += 1
            right += 1
        
        # Refill array A
        for i in range(start, end + 1):
            A[i] = temp[i]
