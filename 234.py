# 1213. Intersection of Three Sorted Arrays. Easy. Contest.

# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
            return []
        one = two = three = 0
        answer = []
        while one < len(arr1) and two < len(arr2) and three < len(arr3):
            if arr1[one] == arr2[two] and arr2[two] == arr3[three]:
                answer.append(arr1[one])
                one += 1
                two += 1
                three += 1
            else:
                if arr1[one] < arr2[two]:
                    one += 1
                elif arr2[two] < arr3[three]:
                    two += 1
                else:
                    three += 1
        return answer
        
# <10 min.
