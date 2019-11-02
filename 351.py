# 5098. Tree Diameter. Medium. Contest.

# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        char = {}
        for e in edges:
            if e[0] not in char:
                char[e[0]] = [e[1]]
            else:
                char[e[0]].append(e[1])
            if e[1] not in char:
                char[e[1]] = [e[0]]
            else:
                char[e[1]].append(e[0])
        
        def virus(l):
            t = 0
            i = 0
            now = [l]
            get = {l : 0}
            while now:
                t += 1
                newnow = []
                for n in now:
                    for m in char[n]:
                        if m not in get:
                            get[m] = t
                            newnow.append(m)
                pre = now
                now = newnow
            return (t - 1, pre)
        
        attempt = virus(0)
        answer = attempt[0]
        for p in attempt[1]:
            new = virus(p)
            answer = max(new[0], answer)
        return answer
