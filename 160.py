

# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# 937. Reorder Data in Log Files. Easy. 55.2%

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def strangekey((s,i)):
            t = 0
            while s[t] != " ":
                t += 1
            s1 = s[t + 1: len(s)] + s[0:t]
            return s1
        
        lets = []
        digs = []
        for i in range(len(logs)):
            t = 0
            while logs[i][t] != " ":
                t += 1
            if ord(logs[i][t + 1]) >= ord("a") and ord(logs[i][t + 1]) <= ord("z"):
                lets.append((logs[i], i))
            else:
                digs.append(logs[i])
        lets.sort(key = strangekey)
        answer = []
        for i in range(len(lets)):
            answer.append(lets[i][0])
        answer.extend(digs)
        return answer
        
# 30min.
