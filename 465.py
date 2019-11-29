# 187. Repeated DNA Sequences. Medium. 37.3%.

# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        char = set()
        for i in range(10, len(s) + 1):
            if s[i - 10 : i] in char:
                answer.add(s[i - 10 : i])
            else:
                char.add(s[i - 10 : i])
        return list(answer)
