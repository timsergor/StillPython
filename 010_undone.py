#Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

class Solution:
    def sortedSquares(self, A: List[int]):
        i = 0
        sl = 1
        sr = 1
        B = []
        while i<len(A) and A[i] < 0:
            i += 1
        if i == len(A):
            for j in range(len(A)):
                B.append(A[len(A)-j-1]*A[len(A)-j-1])
            return(B)    
        B.append(A[i]*A[i]) 
        for j in range(len(A)-1):
            if i - sl < 0:
                i += sr
                sl += sr
                sr = 1
            elif i + sr >= len(A):
                i -= sl
                sr += sl
                sl = 1
            else:
                if abs(A[i-sl]) < abs(A[i+sr]):
                    i -= sl
                    sr += sl
                    sl = 1
                else:
                    i += sr
                    sl += sr
                    sr = 1  
            B.append(A[i]*A[i])     
        return(B)  
