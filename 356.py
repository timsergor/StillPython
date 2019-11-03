# 399. Evaluate Division. Medium. 49.2%.

# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        char = {}
        letters = set()
        for i in range(len(equations)):
            letters.add(equations[i][0])
            letters.add(equations[i][1])
            char[(tuple(equations[i]))] = values[i]
            if values[i]:
                char[(equations[i][1], equations[i][0])] = 1 / values[i]
        
        def solution(q):
            if q[0] in letters and q[1] in letters:
                gone = set()
                wsf  = {}
                wsf[q[0]] = 1
                now = [q[0]]
                while q[1] not in wsf and now:
                    new = []
                    for p in now:
                        for c in letters:
                            if (p,c) in char and (p, c) not in gone and c not in wsf:
                                gone.add((p,c))
                                gone.add((c,p))
                                wsf[c] = wsf[p] * char[(p,c)]
                                new.append(c)
                    now = new
                if q[1] in wsf:
                    return wsf[q[1]]
                else:
                    return -1.0
            else:
                return -1.0
        
        answer = []
        for q in queries:
            answer.append(solution(q))
        return answer
