# 278. First Bad Version. Easy. 31.6%.

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        last = 0
        while n - l > 1:
            if isBadVersion((l + n) // 2):
                n = (l + n) // 2
                last = n
            else:
                l = (l + n) // 2
                last = l
        if last == 0 or l == 1:
            if isBadVersion(1):
                return 1
            else:
                return 2
        return n
