#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#Given two integers x and y, calculate the Hamming distance.

class Solution:
    def hammingDistance(self, x: int, y: int):
        distance = 0
        bit = 1
        for i in range(31):
            if (x == 0) and (y == 0):
                break
            if (x % (bit*2) == 0) and (y % (bit*2)  != 0):
                distance += 1
                y -= bit
            elif (x % (bit*2) != 0) and (y % (bit*2) == 0):
                distance += 1
                x -= bit
            elif (x % (bit*2) != 0) and (y % (bit*2) != 0):
                x -= bit
                y -= bit       
            bit *= 2   
        return(distance)
