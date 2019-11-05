# 477. Total Hamming Distance. Medium. 49.9%.

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Now your job is to find the total Hamming distance between all pairs of the given numbers.

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        answer = 0
        Flag = True
        while Flag:
            Flag = False
            a = 0
            b = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    Flag = True
                if nums[i] % 2:
                    a += 1
                else:
                    b += 1
                nums[i] //= 2
            answer += a * b
        return answer   
