# 1089. Duplicate Zeros. Easy. 58.7%.

# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything from your function. 

from queue import Queue

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        z = 0
        back = Queue()
        for i in range(len(arr)):
            if back:
                if arr[i]:
                    back.put(arr[i])
                else:
                    back.put(0)
                    back.put(0)
                arr[i] = back.get()
            else:
                if arr[i] == 0:
                    back.put(0)
