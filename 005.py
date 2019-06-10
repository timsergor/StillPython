# сокращение всех скобок минимальной глубины
# исходная формулировка: разбить строки на "примитивные" и вывести склейку их содержимого

S = input()
def Reduction(S):
    s =""
    t = 0
    for i in range(len(S)):
        if t == 0:
            t += 1        
        elif t == 1 and S[i]==")":
            t = 0
        else:
            s = s + S[i]
            if S[i] == "(":
                t += 1
            else:
                t -=1    
    return(s)
print(Reduction(S))
