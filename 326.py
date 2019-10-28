# 684. Redundant Connection. Medium. 54%.

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        char = {}
        answer = None
        for l in edges:
            if l[0] in char and l[1] in char[l[0]]:
                return l
            if l[0] not in char and l[1] not in char:
                char[l[0]] = list(l)
                char[l[1]] = char[l[0]]
            elif l[0] not in char:
                char[l[1]].append(l[0])
                char[l[0]] = char[l[1]]
            elif l[1] not in char:
                char[l[0]].append(l[1])
                char[l[1]] = char[l[0]]
            else:
                char[l[0]].extend(char[l[1]])
                for i in char[l[0]]:
                    char[i] = char[l[0]]
        return answer
