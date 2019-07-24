#976. Largest Perimeter Triangle, Easy, 57%

#Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
#If it is impossible to form any triangle of non-zero area, return 0.

def largestPerimeter(A):
    def byfirst(P):
        return(P[0])
    # def IsOne(a,M):
    #     x = M.find(a)
    #     return((x == (len(M) - 1)) or (M[x] != M[x+1]))
    B = []
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                B.append((A[i] + A[j],A[i],A[j]))
            B.sort(key = byfirst)
    A.sort()
    i = 0
    j = 0
    print(B)
    while (i < len(A)) and (j < len(B)) and not((A[i] < B[j][0]) and (A[i] + B[j][1] > B[j][2]) and (A[i] + B[j][2] > B[j][1])) and ((i == (len(A) - 1)) or (A[i] != A[i+1])):
        if (i < len(A) - 1) and (j < len(B) - 1) and A[i + 1] - A[i] < B[j + 1][0] - B[j][0]:
            i += 1
        else:
            j += 1
    if (i == len(A)) or (j == len(B)):
        return(0)
    else:
        return(A[i] + B[j][0],A[i],B[j],i,j,(A[i] + B[j][2] > B[j][1]))
