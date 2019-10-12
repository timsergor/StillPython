# 784. Letter Case Permutation. Easy. 59.4%.

# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        pre = [""]
        for i in range(len(S)):
            answer = []
            if (ord(S[i]) >= ord("a") and ord(S[i]) <= ord("z")):
                for s in pre:
                    answer.append(s + S[i])
                    answer.append(s + chr(ord(S[i]) - ord("a") + ord("A")))
            elif (ord(S[i]) >= ord("A") and ord(S[i]) <= ord("Z")):
                for s in pre:
                    answer.append(s + chr(ord(S[i]) - ord("A") + ord("a")))
                    answer.append(s + S[i])
            else:
                for s in pre:
                    answer.append(s + S[i])
            pre = answer
        return answer
