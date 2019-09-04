#676. Implement Magic Dictionary. Medium. 52.1%.

# Implement a magic directory with buildDict, and search methods.
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

class MagicDictionary(dict):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, dict):
        for c in dict:
            self[c] = True
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        def dist(w1,w2):
            if len(w1) != len(w2):
                return False
            else:
                d = 0
                for i in range(len(w1)):
                    if w1[i] != w2[i]:
                        d += 1
                if d == 1:
                    return True
                else:
                    return False
                
        for w in self:
            if dist(w, word):
                return(True)
        return(False)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

# 15 min
