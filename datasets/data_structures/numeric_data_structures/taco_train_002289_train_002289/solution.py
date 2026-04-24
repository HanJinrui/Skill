t = int(input())
for _ in range(t):
	n = int(input())
	p = []
	for _ in range(n):
		p.append(tuple(map(int, input().split())))
	ans = 0
	for i in range(n):
		d = {}
		for j in range(n):
			if j == i:
				continue
			if p[i][0] - p[j][0] != 0:
				m = (p[i][1] - p[j][1]) / (p[i][0] - p[j][0])
			else:
				m = 10000000000.0
			if m not in d:
				d[m] = 0
			d[m] += 1
			if m == 0:
				m = 10000000000.0
			elif m == 10000000000.0:
				m = 0
			else:
				m = -1 / m
			if m in d:
				ans += d[m]
	print(ans)
