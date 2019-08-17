# 912. Sort an Array. Medium. 63.2%
# Given an array of integers nums, sort the array in ascending order.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(M,N):
            P = []
            i = j = 0
            for k in range(len(M) + len(N)):
                if i == len(M):
                    P.append(N[j])
                    j += 1
                elif j == len(N) or M[i] <= N[j]:
                    P.append(M[i])
                    i += 1
                else:
                    P.append(N[j])
                    j += 1
            return(P)
        
        def sort(nums):
            if len(nums) < 2:
                return(nums)
            else:
                m = len(nums) // 2
                return(merge(sort(nums[0:m]),sort(nums[m:len(nums)])))
        return(sort(nums))
