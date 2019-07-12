#Напишите такую функцию counter(T):
#принимающую на вход кортеж, состоящий из строк латинского алфавита, например, ("ABC", "abc")
#приводящую строки к единому (верхнему, либо нижнему) регистру
#определяющую число уникальных символов латинского алфавита для каждой строки (строка "Aaa" содержит всего 1 уникальный символ)
#возвращающую длину строки с максимальным числом уникальных символов (если таких строк несколько, то самой длинной из них)

def counter(T):
    def decode(s):
        u = []
        d = ord("a") - ord("A")
        for ch in s:
            if ord(ch) < 90:
                u.append(chr(ord(ch)+d))
            else:
                u.append(ch)
        return("".join(u))
    
    def rate(s):
        char = {}
        for ch in s:
            if ch not in char:
                char[ch] = True
        return(len(char))
    
    index = 0
    maxrate = 0
    maxlen = 0
    for i in range(len(T)):
        if rate(decode(T[i])) > maxrate or (rate(decode(T[i])) == maxrate and len(T[i]) > maxlen):
            maxrate = rate(decode(T[i]))
            maxlen = len(T[i])
            index = i
    return(len(T[index])) 
