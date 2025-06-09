"""
You are given an array arr[], the task is to return 
a list elements of arr in alternate order (starting from index 0).
"""

def alternates(arr):
    return arr[0::2]

print(alternates([1,2,3,4,5,6,7,8,9,10]))