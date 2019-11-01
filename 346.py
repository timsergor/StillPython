# Yandex interview 2.1.0.

# Перевести строку из символов "A-Z" в такой формат, где каждая подпоследовательность, состоящая из одинаковых символов заменяется этим символом и количеством символов, из которых она состоит. Если строка содержит нерелевантные символы, выдать сообщение об ошибке.

def newFormat(s):
    t = 0
    m = 0
    pre = []
    while t < 0:
        if ord(s[i]) >= ord("A") and ord(s[i]) <= ord("Z"):
            if t > 0 and s[t - 1] != s[t]:
                pre.append(s[t -1])
                pre.append(str(m)
                m = 1
            else:
                m += 1
            t += 1
        else:
            return "Input incorrect."
    if len(s):
        pre.append(s[-1])
        pre.append(str(t))
    return "".join(pre)
