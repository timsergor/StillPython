# 815. Bus Routes. Hard. 41.3%.

# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

# We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        char = {}
        for r in routes:
            s = set(r)
            for i in range(len(r)):
                if r[i] not in char:
                    char[r[i]] = s
                else:
                    char[r[i]] =  char[r[i]].union(s)
        get = set([S])
        bonder = set([S])
        t = 0
        while bonder and T not in get:
            newbonder = set()
            t += 1
            for s in bonder:
                for f in char[s]:
                    if f not in get:
                        get.add(f)
                        newbonder.add(f)
            bonder = newbonder
        if T in get:
            return t
        else:
            return -1
