# 1229. Meeting Scheduler. Medium. Contest.

# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

# If there is no common time slot that satisfies the requirements, return an empty array.

# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        def myKey(p):
            return p[0]
        
        slots1.sort(key = myKey, reverse = True)
        slots2.sort(key = myKey, reverse = True)
        
        
        while slots1 and slots2 and min(slots1[-1][1], slots2[-1][1]) - max(slots1[-1][0], slots2[-1][0]) < duration:
            if slots2[-1][0] > slots1[-1][1]:
                slots1.pop()
            elif slots1[-1][0] > slots2[-1][1]:
                slots2.pop()
            else:
                if len(slots1) > 1 and len(slots2) > 1:
                    if slots1[-2][0] < slots2[-2][0]:
                        slots1.pop()
                    else:
                        slots2.pop()
                elif len(slots1) > 1:
                    slots1.pop()
                else:
                    slots2.pop()
        
        if slots1 and slots2:
            return [max(slots1[-1][0], slots2[-1][0]), max(slots1[-1][0], slots2[-1][0]) + duration]
        else:
            return []
