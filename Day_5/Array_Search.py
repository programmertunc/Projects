"""
Given an array, arr of n integers, and an integer element x,
find whether element x is present in the array. Return the index of 
the first occurrence of x in the array, or -1 if it doesn't exist.
"""

def array_search(arr,x):
    for i in arr:
        if i == x:
            return arr.index(i)
    else:
        return -1

print(array_search([1,2,3,4,5],3))