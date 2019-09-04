# 677. Map Sum Pairs. Medium. 52.2%.

# Implement a MapSum class with insert, and sum methods.
# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

class MapSum(dict):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        def pref(s,t):
            if len(s) > len(t):
                return False
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
            return True
        
        s = 0
        for c in self:
            if pref(prefix, c):
                s += self[c]
        return(s)
        
# 10min.
