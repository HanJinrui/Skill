(l, d) = ([], {})
for (i, c) in enumerate(input()):
	if c in d:
		(u, v) = ((d[c] + i + 1) // 2, i)
	else:
		l.append(c)
	d[c] = i
s = ''.join(l * 2)
print(s[u:u + 13] + '\n' + s[u + 25:u + 12:-1] if u < v else 'Impossible')
