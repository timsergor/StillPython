# 131. Palindrome Partitioning. Medium. 43.4%.

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        char = {}
        for i in range(len(s)):
            for j in range(min(i + 1, len(s) - i)):
                if s[i - j] == s[i + j]:
                    if i - j in char:
                        char[i - j].append(i + j + 1)
                    else:
                        char[i - j] = [i + j + 1]
                else:
                    break
        for i in range(len(s) - 1):
            for j in range(min(i + 1, len(s) - i - 1)):
                if s[i - j] == s[i + 1 + j]:
                    if i - j in char:
                        char[i - j].append(i + 2 + j)
                    else:
                        char[i - j] = [i + 2 + j]
                else:
                    break
        answer = []
        
        def split(pre, i):
            if i == len(s):
                answer.append(pre)
            else:
                for c in char[i]:
                    split(pre + [s[i:c]], c)
        
        split([], 0)
        return answer
