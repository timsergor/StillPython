# 1269. Number of Ways to Stay in the Same Place After Some Steps. Hard. Contest.

# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place  (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

# Since the answer may be too large, return it modulo 10^9 + 7.

class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        now = [1] + [0] * min((arrLen - 1), steps)
        for i in range(steps):
            dyn = []
            for j in range(len(now)):
                x = now[j]
                if j > 0:
                    x += now[j - 1]
                if j < len(now) - 1:
                    x += now[j + 1]
                dyn.append(x)
            now = dyn
        return dyn[0] % (10 ** 9 + 7)
