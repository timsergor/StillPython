Yandex interview 2.0.1.

# Дан массив из 0 и 1. Из него удаляется один элемент. Какова максимальная последовательность из 1 может остаться после этого в массиве?

def afterReovingLength(M):
    last = 0
    pre = 0
    answer = 0
    for i in range(len(M)):
        if M[i] == 1:
            last += 1
        else:
            if i > 0 and M[i - 1] == 1:
                if last + 2 > i and M[i - last - 2] == 1:
                    answer = max(answer, pre + last)
                else:
                    answer = max(answer, last)
                pre = last
                last = 0
    if len(M) > last:
        if last + 2 > len(M) and M[len(M) - last - 2] == 1:
                answer = max(answer, pre + last)
            else:
                answer = max(answer, last)
    else:
        return last - 1
    return answer
