import heapq
(s, k) = (input(), int(input()))
p = len(s)
l = []
if k > (p + 1) * p // 2:
	print('No such line.')
else:
	for i in range(p):
		heapq.heappush(l, [s[i], i + 1])
	for i in range(k):
		(a, b) = heapq.heappop(l)
		if b < p:
			heapq.heappush(l, [a + s[b], b + 1])
	print(a)
