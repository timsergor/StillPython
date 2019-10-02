# 403. Frog Jump. Hard. 37.1%.

# A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) > 1 and stones[1] != 1:
            return False
        if len(stones) < 2:
            return True
        dyn = [[1],[1]]
        for i in range(1, len(stones) - 1):
            dyn.append([])
        char = {}
        for i in range(len(stones)):
            char[stones[i]] = i
        for i in range(len(stones)):
            for el in dyn[i]:
                if (el - 1 > 0) and (stones[i] + el - 1 in char) and (el - 1 not in dyn[char[stones[i] + el - 1]]):
                    dyn[char[stones[i] + el - 1]].append(el - 1)
                if (stones[i] + el in char) and (el not in dyn[char[stones[i] + el]]):
                    dyn[char[stones[i] + el]].append(el)
                if (stones[i] + el + 1 in char) and (el + 1 not in dyn[char[stones[i] + el + 1]]):
                    dyn[char[stones[i] + el + 1]].append(el + 1)
        return bool(dyn[-1])
        
# 29min.
