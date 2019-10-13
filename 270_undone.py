# 1223. Dice Roll Simulation. Medium. Contest.

# A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

# Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

# Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

 class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        pre = [[1,(0,0,0,0,0,0)]]
        dyn = []
        for k in range(n):
            char = {}
            dyn = []
            for state in pre:
                for i in range(6):
                    if state[1][i] + 1 <= rollMax[i]:
                        newState = []
                        for j in range(6):
                            if j != i:
                                newState.append(state[1][j])
                            else:
                                newState.append(state[1][j] + 1)
                        newState = tuple(newState)
                        if newState not in char:
                            char[newState] = True
                            dyn.append([state[0],newState])
                        else:
                            for s in dyn:
                                if s[1] == newState:
                                    s[0] += state[0]
#                                    break
            pre = list(dyn)
        answer = 0
        for state in dyn:
            answer += state[0]
        return answer % (10**9 + 7)
        
# 25-60min.
