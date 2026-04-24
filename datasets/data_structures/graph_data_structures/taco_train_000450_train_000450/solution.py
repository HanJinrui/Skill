import heapq
import sys
input = sys.stdin.readline
(n, k, s) = map(int, input().split())
(a, pl_al) = (list(map(int, input().split())), {i: [] for i in range(1, k + 1)})
for (i, v) in enumerate(a):
	pl_al[v].append(i)
c = [list(map(int, input().split())) for _ in range(n)]
(heap, costs) = ([(0, a[s - 1])], {})
while heap:
	(cost, al) = heapq.heappop(heap)
	if al in costs:
		continue
	costs[al] = cost
	for pl in pl_al[al]:
		for (i, v) in enumerate(c[pl]):
			if i + 1 not in costs and v != -1:
				heapq.heappush(heap, (cost + v, i + 1))
for v in pl_al:
	if v not in costs:
		costs[v] = -1
print(' '.join((str(costs[v]) for v in a)))
