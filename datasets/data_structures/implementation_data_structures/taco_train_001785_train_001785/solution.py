n = int(input())
d = []
for i in range(n):
	c = input()
	if c == 'pwd':
		print('/' + ''.join(d))
	else:
		for s in c.split()[1].split('/'):
			if not s:
				d = []
			elif s == '..':
				d.pop()
			else:
				d.append(s + '/')
