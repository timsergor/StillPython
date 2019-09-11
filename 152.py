# 347. Top K Frequent Elements. Medium.

# Given a non-empty array of integers, return the k most frequent elements.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def freq(t):
            return t[1]
        
        char = {}
        for n in nums:
            if n not in char:
                char[n] = 1
            else:
                char[n] += 1
        vals = []
        for c in char:
            vals.append((c,char[c]))
        vals.sort(key = freq, reverse = True)
        answer = []
        for i in range(k):
            answer.append(vals[i][0])
        return answer
        
# 10-15 min
