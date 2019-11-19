# 520. Detect Capital. Easy. 52.8%.

# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        Flag1 = ord(word[0]) >= ord("A") and ord(word[0]) <= ord("Z")
        Flag2 = True
        Flag3 = True
        for i in range(1, len(word)):
            Flag2 = Flag2 and ord(word[i]) >= ord("A") and ord(word[i]) <= ord("Z")
            Flag3 = Flag3 and ord(word[i]) >= ord("a") and ord(word[i]) <= ord("z")
        return Flag3 or (Flag1 and Flag2)
