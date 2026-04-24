n = int(input())
v = input()
v = v.replace(' ', '')
d = {'': 0}

def rasklad(s):
	if len(s) == 2:
		return 1
	if s in d:
		return d[s]
	if s[-1] == s[-3] or s[-2] == s[-4]:
		if rasklad(s[0:-4] + s[-2:]):
			d[s] = 1
			return 1
	if len(s) >= 8 and (s[-1] == s[-7] or s[-2] == s[-8]):
		if rasklad(s[0:-8] + s[-2:] + s[-6:-2]):
			d[s] = 1
			return 1
	d[s] = 0
	return 0
print('YES' if rasklad(v) else 'NO')
