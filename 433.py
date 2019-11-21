# 667. Beautiful Arrangement II. Medium. 52.9%.

# Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
# Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

# If there are multiple answers, print any of them.

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def d(k):
            l = []
            for i in range((k + 1) // 2):
                l.append(1 + i)
                l.append((k + 1) - i)
            if (k + 1) % 2:
                l.append((k + 1) // 2 + 1)
            return l
        
        answer = d(k)
        for i in range(k + 2, n + 1):
            answer.append(i)
            
        return answer
