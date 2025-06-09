"""
Given an array arr[], check whether it is sorted in non-decreasing order.
Return true if it is sorted otherwise false.
"""

def sorted(arr):
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True

print(sorted([1,2,3,4,5,5,5]))