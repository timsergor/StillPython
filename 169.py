# 547. Friend Circles. Medium. 55%.

# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def check(M, f, circles, char):
            if f not in char:
                circles += 1
                char[f] = circles
            for i in range(f + 1, len(M)):
                if M[f][i]:
                    if i not in char:
                        char[i] = char[f]
                    elif char[i] < char[f]:
                        x = char[f]
                        for c in char:
                            if char[c] == x:
                                char[c] = char[i]
                    else:
                        x = char[i]
                        for c in char:
                            if char[c] == x:
                                char[c] = char[f]
                        
        circles = 0
        f = 0
        char = {}
        while f < len(M):
            check(M,f,circles,char)
            circles = 0
            for c in char:
                if char[c] > circles:
                    circles = char[c]
            f += 1
        return len(set(char.values()))
