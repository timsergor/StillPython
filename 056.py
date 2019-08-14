#921. Minimum Add to Make Parentheses Valid. Medium. 70.4%

#Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

#Formally, a parentheses string is valid if and only if:

#It is the empty string, or
#It can be written as AB (A concatenated with B), where A and B are valid strings, or
#It can be written as (A), where A is a valid string.
#Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        p = 0
        open = 0
        for i in range(len(S)):
            if S[i] == ")" and open:
                open -= 1
            elif S[i] == ")":
                p += 1
            else:
                open += 1
        return(open + p)
        
 # 10min
