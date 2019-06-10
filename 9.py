#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#Return the element repeated N times.

class Solution:
    def repeatedNTimes(self, A: List[int]):
        char = {}
        for i in range(len(A)):
            if A[i] in char:
                return(A[i])
            else:
                char[A[i]] = True
