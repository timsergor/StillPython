# анаграммы из контеста

s = input()
t = input()
if len(s) != len(t):
	print(0)
else:
	char = {}
	for i in range(len(s)):
		if s[i] not in char:
			char[s[i]] = 1
		else:
			char[s[i]] += 1
		if t[i] not in char:
			char[t[i]] = - 1
		else:
			char[t[i]] -= 1
	Flag = True
	for c in char:
		if char[c] != 0:
			Flag = False
			break
	print(int(Flag))
