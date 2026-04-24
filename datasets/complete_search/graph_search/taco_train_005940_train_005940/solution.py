(n, m) = map(int, input().split())
g = [set() for i in range(n)]
for _ in range(m):
	(a, b) = map(int, input().split())
	g[a - 1].add(b - 1)
	g[b - 1].add(a - 1)
cnt = 0
while True:
	p = set()
	for i in range(n):
		if len(g[i]) == 1:
			p.add(i)
			g[i] = set()
	if len(p) == 0:
		break
	cnt += 1
	for i in range(n):
		g[i] -= p
print(cnt)
