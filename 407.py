# Yandex interview 4.2.1.

# Дан массив с интервалами времени, на которые назначены переговоры. Сколько требуется переговорок, чтобы устроить все эти переговоры.
# input: L = list(tuple(int))

def solution(L):
    M = []
    for i in range(len(L)):
        M.append((L[i][0], 1))
        M.append((L[i][1], -1))
    M.sort()
    answer = t = 0
    for i in range(len(M)):
        t += M[i][1]
        if M[i][0] != M[i - 1][0]:
            answer = max(answer, t)
    return answer
