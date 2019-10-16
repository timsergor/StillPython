# 785. Is Graph Bipartite? Medium. 44.9%.

# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        while len(graph) > 0 and len(graph[-1]) == 0:
            graph.pop()
        if len(graph) < 3:
            return True
        char = {}
        co = {}
        for i in range(len(graph)):
            if len(graph[i]) > 0:
                co[i] = graph[i]
        for i in range(len(graph)):
            if len(graph[i]) > 0:
                char[i] = 0
                break
        
        def paint(z):
            for y in co[z]:
                if y in char and char[y] == char[z]:
                    return False
                else:
                    char[y] = 1 - char[z]
        
        Flag = True
        while len(char) < len(co):
            l = len(char)
            for c in co:
                if c in char:
                    Flag = paint(c)
                    if Flag == False:
                        return False
            if l == len(char):
                for i in range(len(graph)):
                    if i not in char and len(graph[i]) > 0:
                        char[i] = 0
                        break
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if char[i] == char[graph[i][j]]:
                    return False
        return True
