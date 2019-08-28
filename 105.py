#1042. Flower Planting With No Adjacent. Easy. 47.7%.

#You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
#paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
#Also, there is no garden that has more than 3 paths coming into or leaving it.
#Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
#Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        char = {}
        for i in range(len(paths)):
            if paths[i][0] not in char:
                char[paths[i][0]] = [paths[i][1]]
            else:
                char[paths[i][0]].append(paths[i][1])
            if paths[i][1] not in char:
                char[paths[i][1]] = [paths[i][0]]
            else:
                char[paths[i][1]].append(paths[i][0])
        
        flowers = [0] * N
        for i in range(N):
            if i + 1 not in char:
                char[i + 1] = []
            neir = [flowers[j - 1] for j in char[i + 1]]
            if 1 not in neir:
                flowers[i] = 1
            elif 2 not in neir:
                flowers[i] = 2
            elif 3 not in neir:
                flowers[i] = 3
            else:
                flowers[i] = 4
        return flowers
