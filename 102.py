1155. Number of Dice Rolls With Target Sum. Medium. 48.7%.

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        map = [[0] + [1] * f]
        for i in range(1, d):
            map.append([])
            for j in range(target + 1):
                map[-1].append(0)
                map[-1][-1] = sum(map[-2][max(0,j - f):j])
        if d == 1 and target > f:
            return(0)
        return(map[-1][-1] % (10**9 + 7))
        
# < 25min
