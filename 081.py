#6. ZigZag Conversion. Medium. 33.0%.

#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return(s)
        pre = []
        for i in range(numRows):
            for j in range(i,len(s),(2 * (numRows - 1))):
                pre.append(s[j])
                if j + 2 * (numRows - 1) - 2 * i < len(s) and i not in [0,numRows-1]:
                    pre.append(s[j + 2 * (numRows - 1) - 2 * i])
        answer = "".join(pre)
        return(answer)
