# 916. Word Subsets. Medium. 45.9%.

# We are given two arrays A and B of words.  Each word is a string of lowercase letters.
# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
# Now say a word a from A is universal if for every b in B, b is a subset of a. 
# Return a list of all universal words in A.  You can return the words in any order.

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        theChar = {}
        for word in B:
            char = {}
            for s in word:
                if s not in char:
                    char[s] = 1
                else:
                    char[s] += 1
            for s in char:
                if s not in theChar:
                    theChar[s] = char[s]
                else:
                    theChar[s] = max(theChar[s],char[s])
        answer = []
        for word in A:
            char = {}
            for s in word:
                if s not in char:
                    char[s] = 1
                else:
                    char[s] += 1
            Flag = True
            for s in theChar:
                Flag = Flag and (s in char and theChar[s] <= char[s])
            if Flag:
                answer.append(word)
        return answer
        
# 15min.
