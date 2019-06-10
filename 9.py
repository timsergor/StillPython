class Solution:
    def repeatedNTimes(self, A: List[int]):
        char = {}
        for i in range(len(A)):
            if A[i] in char:
                return(A[i])
            else:
                char[A[i]] = True
