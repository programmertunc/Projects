"""
Given an array arr[]. The task is to find the largest element and return it.
"""

def largest(arr):
        # code here
        max = arr[0]
        for i in arr:
            if i>max:
                max = i
        return max

print(largest([5,10,15,16,20,100,2,5,7]))