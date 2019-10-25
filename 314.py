# 1095. Find in Mountain Array. Hard. 34.7%.

# (This problem is an interactive problem.)

# You may recall that an array A is a mountain array if and only if:

# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

# You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        l = mountain_arr.length()
        mem = l + 1
        susp = [0, l - 1]
        right = []
        while susp[1] - susp[0] > 1:
            k = (susp[1] + susp[0]) // 2
            el = mountain_arr.get(k)
            pre = mountain_arr.get(k - 1)
            if el == target and pre < el:
                return k
            elif el == target and pre > el:
                mem = k
                susp = [susp[0], k - 1]
            elif el < target and pre < el:
                susp = [k + 1, susp[1]]
            elif el < target and pre > el:
                if pre == target:
                    mem = k -1
                susp = [susp[0], max(k - 2,0)]
            elif el > target and pre < el:
                if pre == target:
                    return k - 1
                elif pre > target:
                    right = [k + 1, susp[1]]
                    susp = [susp[0], max(k - 2,0)]
                else:
                    susp = [k + 1, susp[1]]
            elif el > target and pre > el:
                right = [k + 1, susp[1]]
                susp = [susp[0], k - 2]
        pre = mountain_arr.get(susp[0])
        if pre == target:
            return susp[0]
        el = mountain_arr.get(susp[1])
        if el == target:
            return susp[1]
        if mem < l:
            return mem
        if not right:
            return -1
        susp = right
        while susp[1] - susp[0] > 1:
            k = (susp1[1] + susp[0]) // 2
            el = mountain_arr.get(k)
            pre = mountain_arr.get(k - 1)
            if el == target:
                return k
            elif el < target:
                susp = [susp[0], k - 1]
            elif el > target:
                susp = [k + 1, susp[1]]
        pre = mountain_arr.get(susp[0])
        if pre == target:
            return susp[0]
        el = mountain_arr.get(susp[1])
        if el == target:
            return susp[1]
        return -1
