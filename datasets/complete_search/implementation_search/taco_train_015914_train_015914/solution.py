I = input
r = range
for _ in [0] * int(I()):
	(n, m) = map(int, I().split())
	s = {ord(x) ^ ((i ^ j) & 1) * 5 for i in r(n) for (j, x) in enumerate(I()) if '.' < x}
	c = s and s.pop() or 82
	print(*(('YES', *(''.join((chr(c ^ ((i ^ j) & 1) * 5) for i in r(m))) for j in r(n))), ['NO'])[bool(s)])
