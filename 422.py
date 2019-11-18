# 394. Decode String. Medium. 47.2%.

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):
            if len(s):
                if ord(s[0]) >= ord("1") and ord(s[0]) <= ord("9"):
                    m = 0
                    while s[m] != "[":
                        m += 1
                    r = m
                    stack = 1
                    while stack:
                        r += 1
                        if s[r] == "[":
                            stack += 1
                        elif s[r] == "]":
                            stack -= 1
                    return int(s[0:m]) * decode(s[m + 1:r]) + decode(s[r + 1:])
                else:
                    r = 1
                    while r < len(s) and not(ord(s[r]) >= ord("0") and ord(s[r]) <= ord("9")):
                        r += 1
                    return s[:r] + decode(s[r:])
            return ""
        
        return decode(s)
