# сколько из этих слов в переводе на азбуку морзе выглядят по-разному?

words = ["gin", "zen", "gig", "msg"]

def translator(word):
    M2 = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    Morse = {}
    for i in range(26):
        Morse[chr(i+97)] = M2[i]
    translation = ""    
    for sb in word:
        translation = translation + Morse[sb]
    return(translation)    

def solution(words):
    Morsewords = {}
    for word in words:
        translation = translator(word)    
        if translation not in Morsewords:
            Morsewords[translation] = True
    return(len(Morsewords))

print(solution(words))
