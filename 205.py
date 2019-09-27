# 17. Letter Combinations of a Phone Number. Medium. 43.1%.

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        buttons = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        layer = [""]
        for i in range(len(digits)):
            nextlayer = []
            for j in range(len(buttons[int(digits[-1 - i])])):
                for word in layer:
                    nextlayer.append(buttons[int(digits[-1 - i])][j] + word)
            layer = nextlayer
        return layer
