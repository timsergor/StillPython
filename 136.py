# 858. Mirror Reflection. Medium. 52.1%

# There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.
# The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.
# Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        point = [p,q]
        Flag = True
        while point[1] % p != 0:
            if Flag:
                if point[0] == p:
                    if p - point[1] >= q:
                        point = [0, point[1] + q]
                    else:
                        point = [0, p - (q +point[1]) % p]
                        Flag = False
                else:
                    if p - point[1] >= q:
                        point = [p, point[1] + q]
                    else:
                        point = [p, p - (q +point[1]) % p]
                        Flag = False
            else:
                if point[0] == p:
                    if point[1] >= q:
                        point = [0, point[1] - q]
                    else:
                        point = [0, abs(point[1] - q)]
                        Flag = True
                else:
                    if point[1] >= q:
                        point = [p, point[1] - q]
                    else:
                        point = [p, abs(point[1] - q)]
                        Flag = True
        if point == [0,p]:
            return 2
        if point == [p,p]:
            return 1
        else:
            return 0
            
 # < 10min.
 
 class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def nod(a,b):
            a, b = max(a,b), min(a,b)
            while a % b != 0:
                a = a % b
                a, b = b, a
            return b
        
        x = p * p
        y = q * p
        z = nod(x,y)
        x = (x/z) % 2
        y = (y/z) % 2
        if x and y:
            return 1
        elif x:
            return 0
        else:
            return 2
            
# < 7 min
