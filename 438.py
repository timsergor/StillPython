# 1048. Longest String Chain. Medium. 51.5%.

# Given a list of words, each word consists of English lowercase letters.

# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

# Return the longest possible length of a word chain with words chosen from the given list of words.

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = len)
        lengths = [0] * len(words[0])
        for i in range(1,len(words)):
            if len(words[i]) != len(words[i - 1]):
                for k in range(len(words[i]) - len(words[i - 1])):
                    lengths.append(i)
        if len(lengths) < 2:
            return 1
        
        def S(a,b):
            if len(a) + 1 == len(b):
                i = 0
                while i < len(a) and a[i] == b[i]:
                    i += 1
                if i < len(a):
                    for j in range(i, len(a)):
                        if a[j] != b[j + 1]:
                            return False
                return True
            return False
        
        score = {}
        answer = 1
        print(words, lengths)
        for i in range(len(words)):
            score[words[i]] = 1
            if i >= lengths[1]:
                for j in range(lengths[len(words[i]) - 2], lengths[len(words[i]) - 1]):
                    if S(words[j], words[i]):
                        score[words[i]] = max(score[words[i]], score[words[j]] + 1)
                answer = max(answer, score[words[i]])
        return answer
