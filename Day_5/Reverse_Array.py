"""You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

"""

def reverseArray(arr):
        # code here
        l = 0
        r = len(arr) -1
        t = 0
        while l<=r:
            t = arr[l]
            arr[l] = arr[r]
            arr[r] = t
            l += 1
            r -= 1
a = [1,0,20,15,2,5]
reverseArray(a)
print(a)