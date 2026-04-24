D = [*map(int, [*open(0)][1].split())]
n = len(D)
r = range
g = [(y + 1) * [0] for y in r(n)]
for d in r(n):
	for i in r(n - d):
		g[d + i][i] = D[i]
	D.remove(d + 1)
for i in r(n):
	print(*g[i])
