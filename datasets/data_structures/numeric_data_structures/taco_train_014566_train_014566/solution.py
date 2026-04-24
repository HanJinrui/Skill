s = input()
t = '#'
for c in s:
	t += c
	if c == t[-2]:
		t = t[:-2]
print('YNEOS'[(len(s) - len(t)) // 2 % 2::2])
