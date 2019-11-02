# 5096. Array Transformation. Easy. Contest.

# Given an initial array arr, every day you produce a new array using the array of the previous day.

# On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:

# If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
# If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
# The first and last elements never change.
# After some days, the array does not change. Return that final array.

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        Flag = False
        new = []
        while arr != new:
            if new:
                arr = new
            new = []
            for i in range(len(arr)):
                if i == 0 or i == len(arr) - 1:
                    new.append(arr[i])
                elif arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                    new.append(arr[i] - 1)
                elif arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
                    new.append(arr[i] + 1)
                else:
                    new.append(arr[i])
        return arr
