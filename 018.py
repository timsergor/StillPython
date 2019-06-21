# Given a matrix A, return the transpose of A.

class Solution:
    def transpose(self, A: List[List[int]]):
        B = []
        for j in range(len(A[0])):
            C = []
            for i in range(len(A)):
                C.append(A[i].pop())
            B.append(C)
        B.reverse()
        return(B)
