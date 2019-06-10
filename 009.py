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
                
class Solution2:
    def repeatedNTimes(self, A: List[int]):
        c = -1
        for i in range(len(A)):
            if c == A[i]:
                return(c)
            c = A[i]
        if A[0] == A[2]:
            return(A[0])
        elif A[0] == A[3]:
            return(A[0])
        return(A[1])                
