import heapq
for _ in range(int(input())):
	a = int(input())
	b = list(map(int, input().split()))
	h = []
	for i in range(a):
		heapq.heappush(h, [-b[i], i + 1])
	li = []
	while 1:
		c = heapq.heappop(h)
		d = heapq.heappop(h)
		if d[0] == 0:
			break
		li += [[c[1], d[1]]]
		c[0] += 1
		d[0] += 1
		heapq.heappush(h, c)
		heapq.heappush(h, d)
	print(len(li))
	for j in li:
		print(*sorted(j))
