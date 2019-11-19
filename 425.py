# 1005. Maximize Sum Of Array After K Negations. Easy. 50.3%.

# Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

# Return the largest possible sum of the array after modifying it in this way.

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        char = {}
        for i in range(len(A)):
            if A[i] in char:
                char[A[i]] += 1
            else:
                char[A[i]] = 1
        for i in range(-100, 0):
            if K == 0:
                break
            if i in char:
                if char[i] <= K:
                    if -i in char:
                        char[-i] += char[i]
                    else:
                        char[-i] = char[i]
                    K -= char[i]
                    char.pop(i)
                else:
                    char[i] -= K
                    if -i in char:
                        char[-i] += K
                    else:
                        char[-i] = K
                    K = 0
        S = 0
        for c in char:
            S += c * char[c]
        if K % 2 == 0 or 0 in char:
            return S
        t = 1
        while t < 101 and t not in char:
            t += 1
        return S - 2 * t
