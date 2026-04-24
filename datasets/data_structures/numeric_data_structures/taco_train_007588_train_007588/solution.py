import heapq
for i in range(int(input())):
	(n, da) = map(int, input().split())
	d = {}
	for i in range(n):
		(x, y, z) = map(int, input().split())
		if x not in d:
			d[x] = []
		d[x].append([-z, y])
	h = []
	for i in range(da):
		if i + 1 in d:
			for i in d[i + 1]:
				heapq.heappush(h, i)
		if h:
			k = heapq.heappop(h)
			if k[-1] > 1:
				k[-1] -= 1
				heapq.heappush(h, k)
	ans = 0
	for i in h:
		ans += i[0] * i[1]
	print(-ans)
