# 824. Goat Latin. Easy. 58%.

#A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

#We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

#The rules of Goat Latin are as follows:

#If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
#If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
#For example, the word "goat" becomes "oatgma".
 
#Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
#Return the final sentence representing the conversion from S to Goat Latin. 

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        T = S.split()
        for i in range(len(T)):
            if T[i][0] == "a" or T[i][0] == "o" or T[i][0] == "e" or T[i][0] == "u" or T[i][0] == "i" or T[i][0] == "A" or T[i][0] == "O" or T[i][0] == "E" or T[i][0] == "U" or T[i][0] == "I":
                T[i] = T[i] + "ma"
            else:
                T[i] = T[i][1:len(T[i])] + T[i][0] + "ma"
            T[i] = T[i] + ("a" * (i+1))
        return(" ".join(T))
        
 # 15 min.       
