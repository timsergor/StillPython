877. Stone Game. Medium. 62%.

#Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
#The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
#Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
#Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:  
        game = []
        step = []
        for j in range(len(piles) - 1):
            step.append(abs(piles[j + 1] - piles[j]))
        game.append(step)
        for i in range(1,len(piles) // 2):
            step = []
            for j in range(len(piles) - 1 - 2 * i):
                step.append(max(piles[j] + min(-piles[j + 1] + game[i - 1][j + 2], - piles[j + 2 * i + 1] + game[i - 1][j + 1]), piles[j + 2 * i + 1] + min(-piles[j] + game[i - 1][j + 1], -piles[j + 2 * i] + game[i - 1][j])))
            game.append(step)
        return(step[0])
        
class Solution:
  return(True)
