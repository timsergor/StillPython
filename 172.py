# 1023. Camelcase Matching. Medium. 54.7%.

# A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

# Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def check(pattern, query):
            if len(pattern) > len(query):
                return False
            if len(pattern) == 0:
                for i in range(len(query)):
                    if ord(query[i]) >= ord("A") and ord(query[i]) <= ord("Z"):
                        return False
                return True
            if pattern[0] == query[0]: 
                return check(pattern[1:len(pattern)], query[1:len(query)])
            else:
                i = 0
                while i < len(query) and (query[i] != pattern[0] and not (ord(query[i]) >= ord("A") and ord(query[i]) <= ord("Z"))):
                    i += 1
                if i == len(query) or not query[i] == pattern[0]:
                    return False
                else:
                    return check(pattern[1:len(pattern)], query[i + 1:len(query)])
                
        answer = []
        for i in range(len(queries)):
            answer.append(check(pattern,queries[i]))
        return answer
