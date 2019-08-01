# 950. Reveal Cards In Increasing Order. Medium. 72.3%

#In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.
#Initially, all the cards start face down (unrevealed) in one deck.
#Now, you do the following steps repeatedly, until all cards are revealed:

#Take the top card of the deck, reveal it, and take it out of the deck.
#If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
#If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
#Return an ordering of the deck that would reveal the cards in increasing order.
#The first entry in the answer is considered to be the top of the deck.

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        l = len(deck)
        new = [0] * l
        head = 0
        tail = 0
        new[head] = deck.pop()
        head += 1
        while deck:
            new[head % l] = deck.pop()
            head += 1
            card = new[tail % l]
            new[tail % l] = 0
            tail += 1
            new[head % l] = card
            head += 1
        deck = []
        for i in range(l):
            deck.append(new[(head - 2 -i) % l])
        return(deck)
