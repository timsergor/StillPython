# 500. Keyboard Row. Easy. 63.2%.

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        s2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        s3 = ["z", "x", "c", "v", "b", "n", "m"]
        answer = []
        
        def good(w):
            if w[0] in s1 or chr(ord(w[0]) - ord("A") + ord("a")) in s1 or chr(ord(w[0]) - ord("a") + ord("A")) in s1:
                for i in range(1, len(w)):
                    if not (w[i] in s1 or chr(ord(w[i]) - ord("A") + ord("a")) in s1 or chr(ord(w[i]) - ord("a") + ord("A")) in s1):
                        return False
                return True
            elif w[0] in s2 or chr(ord(w[0]) - ord("A") + ord("a")) in s2 or chr(ord(w[0]) - ord("a") + ord("A")) in s2:
                for i in range(1, len(w)):
                    if not (w[i] in s2 or chr(ord(w[i]) - ord("A") + ord("a")) in s2 or chr(ord(w[i]) - ord("a") + ord("A")) in s2):
                        return False
                return True
            else:
                for i in range(1, len(w)):
                    if not (w[i] in s3 or chr(ord(w[i]) - ord("A") + ord("a")) in s3 or chr(ord(w[i]) - ord("a") + ord("A")) in s3):
                        return False
                return True
                    
        for w in words:
            if good(w):
                answer.append(w)
        
        return answer
