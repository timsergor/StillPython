# 1276. Number of Burgers with No Waste of Ingredients. Medium. Contest.

# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

# Jumbo Burger: 4 tomato slices and 1 cheese slice.
# Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 0 and tomatoSlices >= 2 * cheeseSlices and tomatoSlices <= 4 * cheeseSlices:
            return [(tomatoSlices - 2 * cheeseSlices) // 2, cheeseSlices - (tomatoSlices - 2 * cheeseSlices) // 2]
        else:
            return []
