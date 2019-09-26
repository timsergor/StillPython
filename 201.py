# 322. Coin Change. Medium. 31.9%.

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        coins.sort()
        map = [0, int(1 in coins)]
        for i in range(2, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0 and (map[i - coins[j]] > 0 or coins[j] == i) and i == len(map):
                    map.append(map[i - coins[j]] + 1)
                elif i - coins[j] >= 0 and i < len(map) and (map[i - coins[j]] > 0 or coins[j] == i) and map[i - coins[j]] + 1 < map[-1]:
                    map[-1] = map[i - coins[j]] + 1
            if i == len(map):
                map.append(0)
        if map[-1]:
            return map[-1]
        else:
            return -1
