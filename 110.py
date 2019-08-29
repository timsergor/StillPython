#66. Plus One. Easy. 41.6%.

#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mem = 0
        digits.reverse()
        for i in range(len(digits)):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                break
        if digits[-1] == 0:
            digits.append(1)
        digits.reverse()
        return(digits)
