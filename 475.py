# 1248. Count Number of Nice Subarrays. Medium. 53.1%.

# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        scheme = []
        t = 1
        for i in range(len(nums)):
            if nums[i] % 2:
                scheme.append(t)
                t = 1
            else:
                t += 1
        scheme.append(t)
        print(scheme)
        answer = 0
        for i in range(len(scheme) - k):
            answer += scheme[i] * scheme[i + k]
        return answer
