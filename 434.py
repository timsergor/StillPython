# 846. Hand of Straights. Medium. 50.6%.

# Alice has a hand of cards, given as an array of integers.

# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

# Return true if and only if she can.

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if W == 1:
            return True
        hand.sort()
        memory = []
        for i in range(len(hand)):
            if not memory:
                memory.append([hand[i], 1])
            else:
                if memory[-1][0] == hand[i]:
                    memory[-1][1] += 1
                else:
                    if hand[i] != memory[-1][0] + 1:
                        return False
                    if len(memory) < W - 1:
                        memory.append([hand[i],1])
                        if len(memory) > 2:
                            if memory[-3][1] > memory[-2][1]:
                                return False
                    else:
                        memory.reverse()
                        for j in range(W - 2, -1, -1):
                            memory[j][1] -= 1
                            if memory[-1][1] == 0:
                                memory.pop()
                        memory.reverse()
        if memory:
            return False
        return True
