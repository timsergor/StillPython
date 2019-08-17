#744. Find Smallest Letter Greater Than Target. Easy. 44.4%

#Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
#Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def dist27(a,b):
            if ord(b) > ord(a):
                return(ord(b) - ord(a))
            else:
                return(ord(b) - ord("a") + 1 + ord("z") - ord(a))
        
        x = letters[0]
        for i in range(1,len(letters)):
            if dist27(target, letters[i]) < dist27(target, x):
                x = letters[i]
        return(x)
        
