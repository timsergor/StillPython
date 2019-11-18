# 934. Shortest Bridge. Medium. 45.4%.

# In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    s = (i,j)
        
        def neir(p):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and p[0] + i >= 0 and p[0] + i < len(A) and p[1] + j >= 0 and p[1] + j < len(A[0]):
                        yield (p[0] + i, p[1] + j)
        
        bound = set()
        island = set([s])
        current = set([s])
        
        while current:
            new = set()
            for p in current:
                for q in neir(p):
                    if A[q[0]][q[1]] == 0:
                        bound.add(p)
                    elif q not in island:
                        island.add(q)
                        new.add(q)
            current = new
        
        answer = 0
        current = bound
        while current:
            new = set()
            for p in current:
                for q in neir(p):
                    if A[q[0]][q[1]] == 1 and q not in island:
                        return answer
                    elif A[q[0]][q[1]] == 0 and q not in island:
                        island.add(q)
                        new.add(q)
            current = new
            answer += 1
