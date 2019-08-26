#491. Increasing Subsequences.Medium. 42.7%.

#Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        IS = []
        for i in range(len(nums)):
            for j in range(len(IS)):
                if IS[j][len(IS[j]) - 1] <= nums[i]:
                    new = list(IS[j])
                    new.append(nums[i])
                    IS.append(new)
            IS.append([nums[i]])
        i = 0
        char = {}
        for S in IS:
            s = tuple(S)
            if s not in char and len(s) > 1:
                char[s] = True
        answer = []
        for s in char:
            answer.append(list(s))
        return(answer)
