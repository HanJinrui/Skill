m = [input() for _ in range(4)]
for l in (m[::-1], m):
	m.append([l[i][i + 1] for i in range(3)])
	m.append([l[i][i] for i in range(4)])
	m.append([l[i + 1][i] for i in range(3)])
	m += zip(*m[:4])
s = ' '.join(map(''.join, m))
print(('NO', 'YES')[any((p in s for p in ('.xx', 'x.x', 'xx.')))])
