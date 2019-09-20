# 856. Score of Parentheses. Medium. 57.5%.

# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def solution(S):
            if S == "()":
                return 1
            depth = 0
            r = 1
            i = 1
            while r > 0:
                if S[i] == "(":
                    r += 1
                else:
                    r -= 1
                i += 1
            if i == len(S):
                return solution(S[1:i - 1]) * 2
            else:
                return solution(S[0:i]) + solution(S[i:len(S)])
        
        return solution(S)
        
# <20min.
