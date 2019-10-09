# 1007. Minimum Domino Rotations For Equal Row. Medium. 51.3%.

# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the i-th domino, so that A[i] and B[i] swap values.

# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

# If it cannot be done, return -1.

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        charA = {1:[],2:[],3:[],4:[],5:[],6:[]}
        charB = {1:[],2:[],3:[],4:[],5:[],6:[]}
        for i in range(len(A)):
            charA[A[i]].append(i)
            charB[B[i]].append(i)
        x = []
        for i in range(1,7):
            s = set(charA[i] + charB[i])
            if len(s) < len(A):
                x.append(-1)
            else:
                x.append(len(A) - max(len(charA[i]),len(charB[i])))
        for i in range(5,-1,-1):
            if x[i] == -1:
                x.pop(i)
        if x:
            return min(x)
        else:
            return -1
