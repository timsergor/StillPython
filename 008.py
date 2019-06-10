#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
odd = []
even = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        even.append(A[i])
    else:
        odd.append(A[i])
print(even+odd)
