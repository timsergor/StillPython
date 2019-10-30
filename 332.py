# 1004. Max Consecutive Ones III. Medium.

# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

# Return the length of the longest (contiguous) subarray that contains only 1s. 

from queue import Queue

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        q = Queue(K + 1)
        answer = 0
        Flag = True
        for i in range(len(A)):
            if A[i] == 0:
                if q.full():
                    Flag = False
                    answer = max(answer, i - q.get() - 1)
                q.put(i)
        if Flag:
            return len(A)
        else:
            return max(answer, i - q.get())
