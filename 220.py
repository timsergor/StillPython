# 1016. Binary String With Substrings Representing 1 To N. Medium. 58.7%.

# Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        n = N
        st = 1
        while n > 1:
            n //= 2
            st += 1
        if len(S) < st:
            return False
        for i in range(st - 1):
            char = {}
            for j in range(len(S) - i):
                if S[j:j + i + 1] not in char and i == 0 or S[j] == "1":
                    char[S[j:j + i + 1]] = True
            if (i == 0 and len(char) != 2) or (i > 0 and len(char) != 2 ** i):
                return False
        char = {}
        for j in range(len(S) - st + 1):
                if S[j:j + st] not in char and S[j] == "1":
                    char[S[j:j + st]] = True
        
        def Bi(n):
            bi = []
            while n > 0:
                bi.append(str(n % 2))
                n //= 2
            bi.reverse()
            return "".join(bi)
        
        D = 2 ** (st - 1)
        for i in range(N - D + 1):
            if Bi(D + i) not in char:
                return False
        return True
