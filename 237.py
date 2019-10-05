# 886. Possible Bipartition. Medium. 41.5%.

# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group. 

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        hate = {}
        for i in range(len(dislikes)):
            if dislikes[i][0] not in hate:
                hate[dislikes[i][0]] = [dislikes[i][1]]
            else:
                hate[dislikes[i][0]].append(dislikes[i][1])
            if dislikes[i][1] not in hate:
                hate[dislikes[i][1]] = [dislikes[i][0]]
            else:
                hate[dislikes[i][1]].append(dislikes[i][0])
        
        for i in range(1,N + 1):
            if i not in hate:
                hate[i] = []
        colours = {}
        t = 1

        def paint1(p):
            if p not in colours:
                colours[p] = 1
                for s in hate[p]:
                    paint2(s)
            elif colours[p] == 2:
                colours[0] = 0

        def paint2(p):
            if p not in colours:
                colours[p] = 2
                for s in hate[p]:
                    paint1(s)
            elif colours[p] == 1:
                colours[0] = 0

        while len(colours) < N:
            t = 1
            while t in colours:
                t += 1
            paint1(t)
        if 0 in colours:
            return False
        return True
