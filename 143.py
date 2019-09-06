# 454. 4Sum II. Medium. 51.4%.

# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        char1 = {}
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] + B[j] not in char1:
                    char1[A[i] + B[j]] = 1
                else:
                    char1[A[i] + B[j]] += 1
        char2 = {}
        for i in range(len(C)):
            for j in range(len(D)):
                if C[i] + D[j] not in char2:
                    char2[C[i] + D[j]] = 1
                else:
                    char2[C[i] + D[j]] +=1
        
        answer = 0
        for c in char1:
            if -c in char2:
                answer += char1[c] * char2[-c]
        return answer
        
# 10min.
