#986. Interval List Intersections. Medium. 

#Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#Return the intersection of these two interval lists.
#(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def Intersection(S1, S2):
            if S1[0] > S2[1]:
                return(1)
            elif S1[1] < S2[0]:
                return(0)
            else:
                return([max(S1[0],S2[0]), min(S1[1], S2[1])])
        
        M = [0,0]
        C = []
        while M[0] < len(A) and M[1] < len(B):
            x = Intersection(A[M[0]],B[M[1]])
            if type(x) is int:
                M[x] += 1
            else:
                C.append(x)
                if A[M[0]][1] > B[M[1]][1]:
                    M[1] += 1
                elif A[M[0]][1] < B[M[1]][1]:
                    M[0] += 1
                else:
                    M[0] += 1
                    M[1] += 1
        return(C)
        
# 30 min
