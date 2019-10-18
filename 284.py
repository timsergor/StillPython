# 647. Palindromic Substrings. Medium. 58.2%.

# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                if i % 2 == 0:
                    for j in range(i // 2 + 1):
                        if s[i // 2 + j] == s[i // 2 - j]:
                            answer += 1
                        else:
                            break
                else:
                    for j in range((i + 1) // 2):
                        if s[(i + 1) // 2 + j] == s[i // 2 - j]:
                            answer += 1
                        else:
                            break
            elif i % 2 == 0:
                for j in range(i // 2 + 1):
                    if s[i // 2 + j] == s[i // 2 - j]:
                        answer += 1
                    else:
                        break
                for j in range(i // 2 + 1):
                    if s[-1 - i // 2 + j] == s[-1 - i // 2 - j]:
                        answer += 1
                    else:
                        break
            else:
                for j in range((i + 1) // 2):
                    if s[(i + 1) // 2 + j] == s[i // 2 - j]:
                        answer += 1
                    else:
                        break
                for j in range((i + 1) // 2):
                    if s[- 1 - (i + 1) // 2 - j] == s[- 1 - i // 2 + j]:
                        answer += 1
                    else:
                        break
        return answer               
