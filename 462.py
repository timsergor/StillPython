# 743. Network Delay Time. Medium. 44.8%.

# There are N network nodes, labelled 1 to N.

# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        char = {}
        for t in times:
            if t[0] not in char:
                char[t[0]] = {t[1] : t[2]}
            else:
                if t[1] in char[t[0]]:
                    char[t[0]][t[1]] = min(char[t[0]][t[1]], t[2])
                else:
                    char[t[0]][t[1]] = t[2]
        for i in range(1, N + 1):
            if i not in char:
                char[i] = {}
        signal = {K : 0}
        prebonder = set([K])
        
        def transmit(k):
            for node in char[k]:
                if node not in signal:
                    signal[node] = signal[k] + char[k][node]
                    bonder.add(node)
                elif signal[node] > signal[k] + char[k][node]:
                    signal[node] = signal[k] + char[k][node]
                    bonder.add(node)                    
        
        while prebonder:
            bonder = set()
            for k in prebonder:
                transmit(k)
            prebonder = bonder
        answer = 0
        for s in signal:
            answer = max(answer, signal[s])
        if len(signal) == N:
            return answer
        else:
            return -1
