# 763. Partition Labels. Medium. 72.2%

# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        char = {}
        for i in range(len(S)):
            if S[i] not in char:
                char[S[i]] = [i]
            else:
                char[S[i]].append(i)
        answer = []
        s = 0
        t = 0
        while s < len(S):
            bag = char[S[t]]
            while max(bag) + 1 - len(bag) != s:
                t += 1
                if t not in bag:
                    bag.extend(char[S[t]])
            answer.append(len(bag))
            s += len(bag)
            t = s
        return answer
