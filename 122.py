#645. Set Mismatch. Easy. 41.1%.

#The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        answer = []
        char = {}
        for i in range(len(nums)):
            if nums[i] not in char:
                char[nums[i]] = True
            else:
                answer.append(nums[i])
        for i in range(1,len(nums) + 1):
            if i not in char:
                answer.append(i)
        return answer
