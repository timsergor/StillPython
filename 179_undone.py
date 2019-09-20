# 126. Word Ladder II

# Share
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.


# TIME LIMIT EXEEDED

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def neir(s,t):
            if len(s) != len(t):
                return False
            let = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    let += 1
                    if let == 2:
                        return False
            if let == 1:
                return True
            return False
        
        steps = {beginWord: [None]}
        if endWord not in wordList:
            return []
        step = 0
        while endWord not in steps:
            add = {}
            for word in wordList:
                if word not in steps:
                    for d in steps:
                        if neir(d,word):
                            if word not in add:
                                add[word] = [d]
                            else:
                                add[word].append(d)
            if len(add) == 0:
                return []
            for word in add:
                steps[word] = add[word]
            step += 1
        preanswer = [[endWord]]
        for i in range(step):
            answer = []
            for path in preanswer:
                for j in range(len(steps[path[-1]])):
                    answer.append(list(path) + [steps[path[-1]][j]])
            preanswer = answer
        for path in preanswer:
            path.reverse()
        return preanswer
