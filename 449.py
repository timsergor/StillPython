# 954. Array of Doubled Pairs. Medium. 35.4%.

# Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def decode(n):
            l = 0
            while n % 2 == 0:
                l += 1
                n //= 2
            return (n, l)
        
        char = {0: []}
        t = 1
        for i in range(len(A)):
            if A[i] == 0:
                char[0].append(t)
                t += 1
            else:
                p = decode(A[i])
                if p[0] in char:
                    char[p[0]].append(p[1])
                else:
                    char[p[0]] = [p[1]]
        for c in char:
            char[c].sort()
            while len(char[c]) > 1:
                t = 0
                x = char[c][-1]
                while char[c] and char[c][-1] == x:
                    char[c].pop()
                    t += 1
                while t and char[c] and char[c][-1] == x - 1:
                    char[c].pop()
                    t -= 1
                if t:
                    return False
            if char[c]:
                return False
        return True
