# 380. Insert Delete GetRandom O(1). Medium. 43.8%.

# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

from random import randint

class RandomizedSet(dict):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxind = -1
        self.map = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self:
            self.maxind += 1
            self[val] = self.maxind
            self.map[self.maxind] = val
            return True
        return False        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self:
            return False
        if self[val] != self.maxind:
            a = self[val]
            self[val], self[self.map[self.maxind]] = self.maxind, self[val]
            self.map[a], self.map[self.maxind] = self.map[self.maxind], self.map[a]
        self.pop(val)
        self.map.pop(self.maxind)
        self.maxind -= 1
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        x = randint(0,self.maxind)
        return self.map[x]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
