# 648. Replace Words. Medium. 54.4%.

# In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

# You need to output the sentence after the replacement.

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        scheme = sentence.split()
        dict.sort(key = len)
        
        def getRoot(word):
            for w in dict:
                if len(word) >= len(w):
                    if word[:len(w)] == w:
                        return w
                else:
                    break
            return False
        
        for i in range(len(scheme)):
            new = getRoot(scheme[i])
            if new:
                scheme[i] = new
        
        return " ".join(scheme)
