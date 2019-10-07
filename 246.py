# 211. Add and Search Word - Data structure design. Medium. 32.1%.

# Design a data structure that supports the following two operations:
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.


class WordDictionary(dict):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lengths = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self[word] = True
        if len(word) not in self.lengths:
            self.lengths[len(word)] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def match(w,sch):
            if len(w) != len(sch):
                return False
            else:
                for i in range(len(w)):
                    if sch[i] != "." and sch[i] != w[i]:
                        return False
                return True
            
        Flag = False
        for s in word:
            if s == ".":
                Flag = True
                break
        if Flag:
            if len(word) not in self.lengths:
                return False
            for c in self:
                if match(c,word):
                    return True
            return False
        else:
            return word in self


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
