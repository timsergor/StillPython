#791. Custom Sort String. Medium. 62.9%

#S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
#S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
#Return any permutation of T (as a string) that satisfies this property.

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order = {}
        for i in range(len(S)):
            if S[i] not in order:
                order[i] = S[i]
        preanswer = []
        char = {}
        for i in range(len(T)):
            if T[i] not in char:
                char[T[i]] = 1
            else:
                char[T[i]] += 1
        for i in range(ord("a"),ord("z")):
            if chr(i) not in char:
                char[chr(i)] = 0
        preanswer = []
        for i in range(len(order)):
            preanswer.extend([order[i]] * char[order[i]])
            char[order[i]] = 0
        for c in char:
            preanswer.extend([c] * char[c])
        return("".join(preanswer))
        
 # 20min
