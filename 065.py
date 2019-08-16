9. Palindrome Number. Easy. 44.4%

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return(False)
        List = []
        while x > 0:
            List.append(x % 10)
            x = x // 10
        for i in range(len(List) // 2):
            if List[i] != List[len(List) - 1 - i]:
                return(False)
        return(True)
