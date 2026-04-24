import heapq
R = lambda : map(int, input().split())
t = int(input())
for _ in range(t):
	(n, a, b, x, y, z) = R()
	c = [-x for x in R()]
	heapq.heapify(c)
	a -= (b - z) // y * x + x
	i = 0
	while a < z and c[0]:
		m = heapq.heappop(c)
		a -= m
		heapq.heappush(c, (m + 1) // 2)
		i += 1
	print((i, 'RIP')[a < z])
