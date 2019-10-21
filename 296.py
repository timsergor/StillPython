# 797. All Paths From Source to Target. Medium. 72.1%.

# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        pre = [[0]]
        char = {}
        while pre:
            nxt = []
            for path in pre:
                for j in graph[path[-1]]:
                    if j == len(graph) - 1:
                        answer.append(path + [j])
                    else:
                        nxt.append(path + [j])
            pre = nxt
        return answer
