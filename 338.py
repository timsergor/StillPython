# 274. H-Index. Medium. 35%.

# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        t = 0
        while t < len(citations) and citations[t] >= t + 1:
            t += 1
        return t
