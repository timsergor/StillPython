# 1215. Stepping Numbers. Medium. Contest.

# A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.

# Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.

class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        hhigh = len(str(high))
        map = [[0,1,2,3,4,5,6,7,8,9]]
        Flag = False
        while len(map) < hhigh:
            next = []
            for i in range(1,10):
                if len(map) > 1:
                    for j in range(len(map[-2])):
                        if map[-2][j] // 10 ** (len(map) - 2) == 1 and i == 1:
                            n = i*(10**len(map)) + map[-2][j]
                            next.append(n)
                            if n >= high:
                                Flag = True
                                break
                for j in range(len(map[-1])):
                    if abs(i - (map[-1][j] // 10 ** (len(map) - 1))) == 1:
                        n = i*(10**len(map)) + map[-1][j]
                        next.append(n)
                        if n >= high:
                            Flag = True
                            break
                if Flag:
                    break
            map.append(next)
        answer = 0
        for i in range(1, len(map)):
            map[0].extend(map[i])
        l = 0
        r = len(map[0]) - 1
        while map[0][l] < low:
            l += 1
        while map[0][r] > high:
            r -= 1
        return map[0][l:r + 1]
        
# 40min.
