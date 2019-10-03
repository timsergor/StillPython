# 33. Search in Rotated Sorted Array. Medium. 33.2%.

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        def search(l,r):
            if r - l < 2:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            if nums[l] < nums[r]:
                if r - l < 2:
                    if nums[l] == target:
                        return l
                    else:
                        return r
                else:
                    if nums[(l + r) // 2] > target:
                        return search(l, ((l + r) // 2) - 1)
                    elif nums[(l + r) // 2] < target:
                        return search(((l + r) // 2) + 1, r)
                    else:
                        return (l + r) // 2
            else:
                if nums[(l + r) // 2] > nums[l]: 
                    if target >= nums[l] and target <= nums[(l + r) // 2]:
                        return search(l,(l + r) // 2)
                    else:
                        return search(((l + r) // 2) + 1, r)
                else:
                    if target >= nums[(l + r) // 2] and target <= nums[r]:
                        return search(((l + r) // 2), r)
                    else:
                        return search(l,(l + r) // 2)
        
        return search(0,len(nums) - 1)
        
# 25min.
