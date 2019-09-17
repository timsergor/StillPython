# 1160. Find Words That Can Be Formed by Characters. Easy. 68.3%.

# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char = {}
        for i in range(len(chars)):
            if chars[i] not in char:
                char[chars[i]] = 1
            else:
                char[chars[i]] += 1
        
        def check(word):
            local = {}
            for i in range(len(word)):
                if word[i] not in char:
                    return False
                else:
                    if word[i] not in local:
                        local[word[i]] = 1
                    else:
                        local[word[i]] += 1
                        if local[word[i]] > char[word[i]]:
                            return False
            return True
        
        answer = 0
        for i in range(len(words)):
            if check(words[i]):
                answer += len(words[i])
        return answer
        
# 6min.
