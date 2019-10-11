# 31. Next Permutation. Medium. 31.2%.

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            pass
        else:
            if nums[-1] > nums[-2]:
                nums[-1], nums[-2]  = nums[-2], nums[-1]
            else:
                t = len(nums) - 1
                while t > 0 and nums[t] <= nums[t - 1]:
                    t -= 1
                if t == 0:
                    nums.reverse()
                else:
                    k = t + 1
                    while k < len(nums) and nums[k] > nums[t - 1]:
                        k += 1
                    nums[k - 1], nums[t - 1] = nums[t - 1], nums[k - 1]
                    for i in range((len(nums) - t) // 2):
                        nums[t + i], nums[-1 - i] = nums[-1 - i], nums[t + i]
