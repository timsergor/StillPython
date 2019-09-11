# 22. Generate Parentheses. Medium. 56.9%.
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        all = [[""]]
        for i in range(n):
            next = []
            for j in range(len(all)):
                for l in range(len(all[-1 - j])):
                    for r in range(len(all[j])):
                        s = "(" + all[-1 - j][l] + ")" + all[j][r]
                        next.append(s)
            all.append(next)
        return all[-1]
