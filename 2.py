#сколько в строке камней s драгоценных камней из j

def solve(j,s):
    answer = 0
    jems = {}
    for ch in j:
        jems[ch] = True
    for ch in s:
        if ch in jems:
            answer += 1
    return(answer)
j = input()
s = input()
print(solve(j,s))
