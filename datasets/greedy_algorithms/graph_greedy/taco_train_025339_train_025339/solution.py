import sys
input = sys.stdin.readline
import heapq
(n, m, k) = map(int, input().split())
adj = [[] for _ in range(n + 5)]
for _ in range(m):
	(u, v, w) = map(int, input().split())
	adj[u].append((v, w))
	adj[v].append((u, w))
train = [-1 for _ in range(n + 5)]
ans = 0
dist = [int(1000000000000000.0) for _ in range(n + 5)]
pq = []
for _ in range(k):
	(s, y) = map(int, input().split())
	if train[s] != -1:
		ans += 1
		train[s] = min(train[s], y)
		dist[s] = train[s]
		continue
	train[s] = y
	dist[s] = y
for i in range(n + 5):
	if dist[i] != -1:
		heapq.heappush(pq, (dist[i], i))
heapq.heappush(pq, (0, 1))
dist[1] = 0
cut = [0 for _ in range(n + 5)]
vis = [0 for _ in range(n + 5)]
while pq:
	(dummy, u) = heapq.heappop(pq)
	if vis[u]:
		continue
	vis[u] = 1
	for (v, w) in adj[u]:
		if dist[v] >= dist[u] + w:
			if dist[v] != dist[u] + w:
				heapq.heappush(pq, (dist[u] + w, v))
			dist[v] = dist[u] + w
			if train[v] != -1:
				cut[v] = 1
for b in cut:
	if b == 1:
		ans += 1
print(ans)
