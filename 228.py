# 809. Expressive Words. Medium. 44.9%.

# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

# For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

# Given a list of query words, return the number of words that are stretchy. 

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def code(word):
            C = []
            for i in range(len(word)):
                if i == 0 or word[i] != word[i-1]:
                    C.append([word[i],1])
                else:
                    C[-1][-1] += 1
            return C
        theCode = code(S)
        answer = 0
        for word in words:
            aCode = code(word)
            if len(aCode) == len(theCode):
                Flag = True
                for i in range(len(aCode)):
                    Flag = (aCode[i][0] == theCode[i][0]) and (theCode[i][1] >= 3 and aCode[i][1] <= theCode[i][1] or theCode[i][1] == aCode[i][1])
                    if not Flag:
                        break
                    if Flag and i == len(aCode) - 1:
                        answer += 1
        return answer
