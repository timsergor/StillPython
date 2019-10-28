# 835. Image Overlap. Medium. 54.4%.

# Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

# (Note also that a translation does not include any kind of rotation.)

# What is the largest possible overlap?

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        dist = {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                for k in range(len(B)):
                    for l in range(len(B[0])):
                        if A[i][j]  and B[k][l]:
                            if ((k - i), (l - j)) not in dist:
                                dist[((k - i), (l - j))] = 1
                            else:
                                dist[((k - i), (l - j))] += 1
        answer = 0
        for c in dist:
            answer = max(dist[c],answer)
        return answer
