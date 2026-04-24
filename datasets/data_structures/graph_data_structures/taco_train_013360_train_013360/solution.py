import heapq
(n, m) = [int(x) for x in input().split()]
a = [[] for i in range(n)]
for i in range(m):
	(p, q) = [int(x) for x in input().split()]
	if p == q:
		continue
	a[p - 1].append((0, q - 1))
	a[q - 1].append((1, p - 1))
d = [-1] * n
d[0] = 0
q = a[0]
heapq.heapify(q)
while q:
	p = heapq.heappop(q)
	for x in a[p[1]]:
		if d[x[1]] == -1 or d[x[1]] > p[0] + x[0]:
			d[x[1]] = p[0] + x[0]
			heapq.heappush(q, (d[x[1]], x[1]))
print(d[n - 1])
