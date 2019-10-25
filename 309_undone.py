# 1177. Can Make Palindrome from Substring. Medium. 32.4%.

# Given a string s, we make queries on substrings of s.

# For each query queries[i] = [left, right, k], we may rearrange the substring s[left], ..., s[right], and then choose up to k of them to replace with any lowercase English letter. 

# If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

# Return an array answer[], where answer[i] is the result of the i-th query queries[i].

# Note that: Each letter is counted individually for replacement so if for example s[left..right] = "aaa", and k = 2, we can only replace two of the letters.  (Also, note that the initial string s is never modified by any query.)

TIME LIMIT EXEEDED

class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        scheme = [{}]
        char = {}
        for i in range(len(s)):
            if s[i] not in char:
                char[s[i]] = 1
            else:
                char[s[i]] += 1
            scheme.append(dict(char))
        answer = []
        for q in queries:
            char = {}
            for c in scheme[q[1] + 1]:
                if c not in scheme[q[0]]:
                    char[c] = scheme[q[1] + 1][c]
                else:
                    char[c] = scheme[q[1] + 1][c] - scheme[q[0]][c]
            problems = 0
            for c in char:
                if char[c] % 2:
                    problems += 1
            answer.append(q[2] >= problems // 2)
        return answer
