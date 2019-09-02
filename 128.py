# 540. Single Element in a Sorted Array. Medium. 57.5%.

#Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once. Find this single element that appears only once.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def solution(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                if (len(nums) // 2) % 2 == 1:
                    if nums[len(nums) // 2] == nums[len(nums) // 2 + 1]:
                        return solution(nums[0:len(nums) // 2])
                    else:
                        return solution(nums[len(nums) // 2 + 1:len(nums)])
                else:
                    if nums[len(nums) // 2] == nums[len(nums) // 2 + 1]:
                        return solution(nums[len(nums) // 2:len(nums)])
                    else:
                        return solution(nums[0:len(nums) // 2 + 1])
        return solution(nums)
