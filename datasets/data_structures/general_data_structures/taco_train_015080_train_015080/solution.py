for _ in range(int(input())):
	(n, m) = map(int, input().split())
	a = []
	for i in range(n):
		a += [input()]
	p = n
	q = -1
	r = m
	s = -1
	for i in range(n):
		for j in range(m):
			if a[i][j] == '*':
				p = min(i, p)
				q = max(i, q)
				r = min(j, r)
				s = max(j, s)
	if q >= 0:
		print((max(q - p, s - r) + 1) // 2 + 1)
	else:
		print(0)
