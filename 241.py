# 733. Flood Fill. Easy. 51.9%.

# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def neir(pixel):
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i + j) == 1 and pixel[0] + i >= 0 and pixel[0] + i < len(image) and pixel[1] + j >= 0 and pixel[1] + j < len(image[0]):
                        yield((pixel[0] + i, pixel[1] + j))
        
        char = {}
        def paint(pixel,oldColor,newColor):
            if image[pixel[0]][pixel[1]] == oldColor:
                image[pixel[0]][pixel[1]] = newColor
                char[pixel] = True
                for p in neir(pixel):
                    if p not in char:
                        paint(p,oldColor,newColor)
        
        paint((sr,sc),image[sr][sc],newColor)
        
        return image
