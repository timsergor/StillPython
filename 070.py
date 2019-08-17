#1128. Number of Equivalent Domino Pairs. Easy. 44.4%.

#Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.
#Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        char = {}
        for i in range(len(dominoes)):
            if dominoes[i][0] <= dominoes[i][1]:
                if (dominoes[i][0], dominoes[i][1]) not in char:
                    char[(dominoes[i][0], dominoes[i][1])] = 1
                else:
                    char[(dominoes[i][0], dominoes[i][1])] += 1
            else:
                if (dominoes[i][1], dominoes[i][0]) not in char:
                    char[(dominoes[i][1], dominoes[i][0])] = 1
                else:
                    char[(dominoes[i][1], dominoes[i][0])] += 1
        pairs = 0
        for c in char:
            pairs += char[c] * (char[c] - 1) // 2
        return(pairs)
