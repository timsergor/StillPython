# 93. Restore IP Addresses. Medium. 32.7%.

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer = []
        if len(s) < 4:
            return answer
        
        def isNumber(n):
            return (n[0] != "0" or len(n) == 1) and int(n) <= 255
        
        def solution(s, k, back = ""):
            if k == 0:
                if isNumber(s):
                    answer.append(back + "." + s)
            else:
                for i in range(1,4):
                    if isNumber(s[:i]) and len(s) - i <= 3 * k and len(s) - i >= k:
                        if k < 3:
                            solution(s[i:], k - 1, back + "." + s[:i])
                        else:
                            solution(s[i:], k - 1, s[:i])
        solution(s, 3)
        return answer
