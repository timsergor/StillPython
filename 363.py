# 486. Predict the Winner. Medium. 47.1%.

# Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

# Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        dyn = []
        for i in range(len(nums) - 1):
            dyn.append(max(nums[i], nums[i + 1]) - min(nums[i], nums[i + 1]))
        while len(dyn) > 1:
            new = []
            for i in range(len(dyn) - 1):
                new.append(max(nums[(len(nums) - len(dyn)) + i + 1] - dyn[i], nums[i] - dyn[i + 1]))
            dyn = new
        return dyn[0] >= 0
