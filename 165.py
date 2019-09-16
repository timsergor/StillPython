# 997. Find the Town Judge. Easy. 49.5%.

# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        char = {}
        charj = {}
        for i in range(len(trust)):
            charj[trust[i][0]] = True
            if trust[i][1] not in char:
                char[trust[i][1]] = [trust[i][0]]
            else:
                char[trust[i][1]].append(trust[i][0])
        judge = -1
        for i in range(1,N + 1):
            if i in char:
                if len(char[i]) == N - 1 and i not in charj:
                    if judge == -1:
                        judge = i
                    else:
                        return -1
        return judge
        
# 13min.
