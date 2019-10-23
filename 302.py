# 848. Shifting Letters. Medium. 42.4%.

# We have a string S of lowercase letters, and an integer array shifts.

# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

# Return the final string after all such shifts to S are applied.

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i + 1]) % 26
        pre = []
        for i in range(len(shifts)):
            if ord(S[i]) + shifts[i] % 26 <= ord("z"):
                pre.append(chr(ord(S[i]) + shifts[i] % 26))
            else:
                pre.append(chr(ord(S[i]) + shifts[i] % 26 - 26))
        return "".join(pre)
        
# 10min.
