# 1073. Adding Two Negabinary Numbers. Medium. 32.1%.

# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if len(arr2) > len(arr1):
            arr1, arr2 = arr2, arr1
        arr1.reverse()
        arr2.reverse()
        answer = []
        mem = 0
        for i in range(len(arr1)):
            if len(arr2) <= i:
                i2 = 0
            else:
                i2 = arr2[i]
            answer.append((int(bool(mem)) + arr1[i] + i2) % 2)
            if mem == 0:
                if arr1[i] + i2 == 2:
                    mem = 2
            elif mem == 1:
                if arr1[i] + i2 >= 1:
                    mem = 2
                else:
                    mem = 0
            elif mem == 2:
                if arr1[i] + i2 == 0:
                    mem = 1
                else:
                    mem = 0
        while mem:
            answer.append(1)
            mem -= 1
        while answer[-1] == 0 and len(answer) > 1:
            answer.pop()
        answer.reverse()
        return answer
