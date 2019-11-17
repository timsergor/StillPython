# 802. Find Eventual Safe States. Medium. 46.1%.

# In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

# Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

# Which nodes are eventually safe?  Return them as an array in sorted order.

# The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        pre = set()
        t = -1
        while t != len(pre):
            t = len(pre)
            for i in range(len(graph)):
                Flag = True
                for j in range(len(graph[i])):
                    if graph[i][j] not in pre:
                        Flag = False
                        break
                if Flag:
                    pre.add(i)
        answer = list(pre)
        answer.sort()
        return answer
