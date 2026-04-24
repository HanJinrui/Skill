for _ in range(int(input())):
	s = input()
	p = input()
	u = []
	u.append(p[0])
	for i in p[1:]:
		if i not in u:
			u.append(i)
	s += p[0]
	s = ''.join(sorted(s))
	for i in p:
		s = s.replace(i, '', 1)
	x = 0
	if u[0] < u[1]:
		x = s.rfind(p[0])
	else:
		x = s.find(p[0])
	print(s[:x] + p + s[x + 1:])
