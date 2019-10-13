# 1221. Split a String in Balanced Strings. Easy. Contest.

# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        answer = 0
        for i in range(len(s)):
            if s[i] == "L":
                l += 1
            else:
                r += 1
            if l == r:
                answer +=1
        return answer
        
# ~5min.
