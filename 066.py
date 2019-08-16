#338. Counting Bits. Medium. 65.4%.

#Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

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

# < 15 min
