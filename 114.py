482. License Key Formatting. Easy. 41.4%.

#You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.
#Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.
#Given a non-empty string S and a number K, format the string according to the rules described above.

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        preanswer = []
        counter = 0
        for i in range(len(S)):
            if S[-1-i] != "-":
                if ord(S[-1-i]) >= ord("a") and ord(S[-1-i]) <= ord("z"):
                    preanswer.append(chr(ord(S[-1-i]) + ord("A") - ord("a")))
                else:
                    preanswer.append(S[-i-1])
                counter = (counter + 1) % K
                if counter == 0:
                    preanswer.append("-")
        if len(preanswer) > 0 and preanswer[-1] == "-":
            preanswer.pop()
        preanswer.reverse()
        return("".join(preanswer))
