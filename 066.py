class Solution:
    def countBits(self, num: int) -> List[int]:
        def solution(num):
            if num == 0:
                return([0])
            elif num == 1:
                return([0,1])
            else:
                array = solution(1)
                while len(array) < num + 1:
                    array2 = []
                    for i in range(len(array)):
                        array2.append(array[i] + 1)
                        if len(array) + len(array2) == num + 1:
                            break
                    array.extend(array2)
            return(array)
        return(solution(num))
