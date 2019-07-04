# в массиве натуральных чисел найти подотрезок чисел с данной суммой

def interval(M,Sum):
    l = 0
    r = 0
    s = M[0]
    while l < len(M):
        if s < Sum:
            r += 1
            s += M[r]
        elif s == Sum:
            return(l,r)
        else:
            if l < r:
                s -= M[l]
                l += 1
            else:
                s -= M[l]
                l += 1
                r += 1
                s += M[r]
    return(None)
