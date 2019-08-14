504. Base 7. Easy. 45.1%
Given an integer, return its base 7 string representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        def solution(num):
            result = 0
            seven = [1]
            while seven[len(seven)-1] <= num:
                seven.append(seven[len(seven)-1]*7)
            seven.pop()
            while seven:
                if seven[len(seven) - 1] <= num:
                    result += num // seven[len(seven) - 1]
                    result *= 10
                    num -= (num // seven[len(seven)-1]) * seven[len(seven)-1]
                    seven.pop()
                else:
                    result *= 10
                    seven.pop()
            return(result // 10)
        
        if num >= 0:
            return(str(solution(num)))
        else:
            return("-" + str(solution((-1) * num)))
