# 5109. Smallest Common Region. Medium. Contest.

# You are given some lists of regions where the first region of each list includes all other regions in that list.

# Naturally, if a region X contains another region Y then X is bigger than Y.

# Given two regions region1, region2, find out the smallest region that contains both of them.

# If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        back = {}
        for r in regions:
            for i in range(1, len(r)):
                back[r[i]] = r[0]
            if r[0] not in back:
                back[r[0]] = "#"
                
        B = set()
        while region1 in back:
            B.add(region1)
            region1 = back[region1]
        while region2 not in B:
            region2 = back[region2]
        return region2
