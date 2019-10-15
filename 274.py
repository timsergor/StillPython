# 386. Lexicographical Numbers. Medium. 48.2%.

# Given an integer n, return 1 - n in lexicographical order.

# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        r = list(range(1,n + 1))
        for i in range(n):
            r[i] = str(r[i])
        r.sort()
        for i in range(n):
            r[i] = int(r[i])
        return r
