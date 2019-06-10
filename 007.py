# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
M = [[1,1,0],[1,0,1],[1,1,1]]
for i in range(len(M)):
    M[i].reverse()   
    for j in range(len(M[i])):
        M[i][j] = 1 - M[i][j] 
print(M)
