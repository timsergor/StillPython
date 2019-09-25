# 171. Excel Sheet Column Number. Easy. 52.4%.

# Given a column title as appear in an Excel sheet, return its corresponding column number.

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        for i in range(len(s)):
            answer += (ord(s[-1 -i]) - ord("A") + 1)*(26**i)
        return answer
