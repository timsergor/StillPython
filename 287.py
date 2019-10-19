# 1230. Toss Strange Coins. Medium. Contest.

# You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.

# Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        map = [[1] + [0] * target]
        for i in range(len(prob)):
            map.append([])
            for j in range(target + 1):
                if j == 0:
                    map[-1].append(map[-2][0] * (1 - prob[i]))
                else:
                    map[-1].append(map[-2][j] * (1 - prob[i]) + map[-2][j - 1] * prob[i])
        return map[-1][-1]
