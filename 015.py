#Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#If S[i] == "I", then A[i] < A[i+1]
#If S[i] == "D", then A[i] > A[i+1]

class Solution:
    def diStringMatch(self, S: str):
        a = 0
        b = len(S)
        A = []
        for i in range(len(S)):
            if S[i] == "I":
                A.append(a)
                a += 1
            else:    
                A.append(b)
                b -= 1
        A.append(a)        
        return(A)        
