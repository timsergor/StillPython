# 884. Uncommon Words from Two Sentences. Easy. 61.4%.

# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Return a list of all uncommon words. 

# You may return the list in any order.

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split()
        C = {}
        for w in A:
            if w in C:
                C[w] += 1
            else:
                C[w] = 1
        for w in B:
            if w in C:
                C[w] += 1
            else:
                C[w] = 1
        answer = []
        for w in C:
            if C[w] == 1:
                answer.append(w)
        return answer
