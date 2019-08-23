#819. Most Common Word. Easy. 42.4%.
#Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        List = []
        word = []
        for i in range(len(paragraph)):
            if ord(paragraph[i]) >= ord("a") and ord(paragraph[i]) <= ord("z"):
                word.append(paragraph[i])
            elif ord(paragraph[i]) >= ord("A") and ord(paragraph[i]) <= ord("Z"):
                word.append(chr(ord(paragraph[i]) + ord("a") - ord("A")))
            elif len(word) > 0:
                List.append("".join(word))
                word = []
        if (ord(paragraph[len(paragraph) - 1]) >= ord("a") and ord(paragraph[len(paragraph) - 1]) <= ord("z")) or (ord(paragraph[len(paragraph) - 1]) >= ord("A") and ord(paragraph[len(paragraph) - 1]) <= ord("Z")):
            List.append("".join(word))
            word = []
        banchar = {word:True for word in banned}
        char = {}
        for word in List:
            if word not in banchar:
                if word not in char:
                    char[word] = 1
                else:
                    char[word] += 1
                    
        m = 0
        for word in char:
            if char[word] > m:
                w = word
                m = char[word]
        return(w)
