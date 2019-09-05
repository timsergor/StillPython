# 1035. Uncrossed Lines. Medium. 51.9%.

# We write the integers of A and B (in the order they are given) on two separate horizontal lines.
# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
# Return the maximum number of connecting lines we can draw in this way.

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        result = [[[0,-1,-1]] * (len(B) + 1)]
        for i in range(len(A)):
            result.append([[0,-1,-1]])
            for j in range(len(B)):
                if B[j] == A[i] and i > result[i][j][1] and j > result[i][j][2]:
                    result[-1].append([result[i][j][0] + 1, i, j])
                else:
                    a = result[i][j][0]
                    b = result[i][j + 1][0]
                    c = result[i + 1][j][0]
                    if a == max(a,b,c):
                        result[-1].append(result[i][j])
                    elif b == max(a,b,c):
                        result[-1].append(result[i][j + 1])
                    else:
                        result[-1].append(result[i + 1][j])
        m = result[-1][0][0]
        for i in range(1,len(B) + 1):
            if result[-1][i][0] > m:
                m = result[-1][i][0]
        for i in range(len(A) + 1):
            if result[i][-1][0] > m:
                m = result[i][-1][0]
        return m
