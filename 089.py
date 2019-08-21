#442. Find All Duplicates in an Array. Medium. 62%.

#Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#Find all the elements that appear twice in this array.
#Could you do it without extra space and in O(n) runtime?

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums2 = []
        char = {}
        for i in nums:
            if i in char:
                nums2.append(i)
            else:
                char[i] = True
        return(nums2)
        
# 2min
