# 798. Smallest Rotation with Highest Score. Hard. 41.4%.

# Given an array A, we may rotate it by a non-negative integer K so that the array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].  Afterward, any entries that are less than or equal to their index are worth 1 point. 

# For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

# Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If there are multiple answers, return the smallest such index K.

class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        char = {}
        for i in range(len(A)):
            if ((i - A[i]) % len(A), "right") in char:
                char[((i - A[i]) % len(A), "right")] += 1
            else:
                char[((i - A[i]) % len(A), "right")] = 1
            if (i + 1, "left") in char:
                char[((i + 1) % len(A), "left")] += 1
            else:
                char[((i + 1) % len(A), "left")] = 1
        best = 0
        for i in range(len(A)):
            if A[i] <= i:
                best += 1
        score = best
        answer = 0
        for i in range(1,len(A)):
            if (i,"left") in char:
                score += char[(i,"left")]
            if (i - 1,"right") in char:
                score -= char[(i - 1,"right")]
            if score > best:
                best = score
                answer = i
        return answer
