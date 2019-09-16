# 455. Assign Cookies. Easy. 48.8%.

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        con = 0
        gi = 0
        si = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                con += 1
                si += 1
                gi += 1
            else:
                si += 1
        return con
        
# < 5min.
