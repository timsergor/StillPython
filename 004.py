#перевести большие буквы в маленькие, остальные не трогать

str = input()
t =""
for i in range(len(str)):
    if ord(str[i]) >= 97 or ord(str[i])<= 64:
        t = t + str[i]
    else:
        t = t + chr(ord(str[i])+32)
print(t)
