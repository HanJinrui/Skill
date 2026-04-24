from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
g = [[] for i in range(n + 1)]
for _ in range(m):
	(u, v, w) = map(int, input().split())
	g[u].append((v, w * 2))
	g[v].append((u, w * 2))
a = [''] + list(map(int, input().split()))
ans = a.copy()
hp = [(a[i], i) for i in range(1, n + 1)]
heapify(hp)
while hp:
	(dcur, cur) = heappop(hp)
	if dcur > ans[cur]:
		continue
	for (v, w) in g[cur]:
		if dcur + w < ans[v]:
			ans[v] = dcur + w
			heappush(hp, (ans[v], v))
print(*ans[1:])
