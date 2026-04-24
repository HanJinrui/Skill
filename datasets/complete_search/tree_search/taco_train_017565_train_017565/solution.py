t = int(input())
for T in range(t):
	(n, d) = map(int, input().strip().split())
	u = (n - 1) * n // 2
	if d > u:
		print('NO')
		continue
	l = t = 0
	for i in range(1, 1 + n):
		l += t
		if not i & i + 1:
			t += 1
	if d < l:
		print('NO')
		continue
	p = [1] * n
	l = [1 << i for i in range(n)]
	o = n - 1
	while u > d:
		m = o
		while u > d and m and (p[m - 1] < l[m - 1]):
			m -= 1
			u -= 1
		p[o] -= 1
		p[m] += 1
		o -= 1
	r = [0] * n
	c = [1, 1]
	t = []
	v = 1
	for i in range(1, n):
		if not p[i]:
			break
		for j in range(p[i]):
			r[v] = c.pop()
			v += 1
			t.append(v)
			t.append(v)
		c = t
		t = []
	print('YES')
	print(*(r[i] for i in range(1, n)))
