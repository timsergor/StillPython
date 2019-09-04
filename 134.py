# 781. Rabbits in Forest. Medium.

# In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.
# Return the minimum number of rabbits that could be in the forest.

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        answer = 0
        char = {}
        for i in answers:
            if i not in char:
                char[i] = 1
            else:
                char[i] += 1
        for i in char:
            while char[i] % (i + 1):
                char[i] += 1
            answer += char[i]
        return answer
        
# 5min
