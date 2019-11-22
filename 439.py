# 1046. Last Stone Weight. Easy. 62.4%.

# We have a collection of rocks, each rock has a positive integer weight.

# Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            smash = []
            for i in range(len(stones)):
                if len(smash) < 2:
                    smash.append(stones[i])
                elif stones[i] > min(smash):
                    smash.remove(min(smash))
                    smash.append(stones[i])
            stones.remove(smash[0])
            stones.remove(smash[1])
            if smash[0] != smash[1]:
                stones.append(abs(smash[0] - smash[1]))
        if stones:
            return stones[0]
        return 0
