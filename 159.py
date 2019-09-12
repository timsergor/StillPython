# 42. Trapping Rain Water. Hard. 44.6%.

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        la = []
        ra = []
        l = r = 0
        for i in range(len(height)):
            if l > height[i]:
                la.append(l - height[i])
            else:
                l = height[i]
                la.append(0)
            if r > height[-1 - i]:
                ra.append(r - height[-1 - i])
            else:
                r = height[-1 - i]
                ra.append(0)
        answer = 0
        for i in range(len(height)):
            answer += min(la[i],ra[-1 - i])
        return answer 
        
# 9min.
