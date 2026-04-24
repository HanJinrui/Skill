def snek(k, n, x, d, g):
	if k == n:
		x += [d[n]]
		return
	for i in range(1, n + 1):
		if g[k][i] != 0 and d[i] == -1:
			d[i] = d[k] + g[k][i]
			snek(i, n, x, d, g)
			d[i] = -1
t = int(input())
for i in range(t):
	g = [[0 for i in range(11)] for j in range(11)]
	(v, e) = map(int, input().split())
	for j in range(e):
		(x, y, w) = map(int, input().split())
		g[x][y] = w
		g[y][x] = w
	x = []
	d = [-1] * (v + 1)
	d[1] = 0
	snek(1, v, x, d, g)
	x.sort()
	r = x[0]
	ans = 0
	for z in range(len(x)):
		if r == x[z]:
			ans += 1
	print(ans)
