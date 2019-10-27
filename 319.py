# 1238. Circular Permutation in Binary Representation. Medium. Contest.

# Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :

# p[0] = start
# p[i] and p[i+1] differ by only one bit in their binary representation.
# p[0] and p[2^n -1] must also differ by only one bit in their binary representation.

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def solution(n):
            if n == 1:
                return [0, 1]
            L = solution(n - 1)
            R = list(L)
            for i in range(len(R)):
                R[i] += 2 ** (n - 1)
            R.reverse()
            return L + R
        
        t = 0
        S = solution(n)
        while S[t] != start:
            t += 1
        return S[t:] + S[:t]
