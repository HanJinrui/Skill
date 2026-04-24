import heapq as h
INF = 1001001001
(N, M) = map(int, input().split())
G = [[] for _ in range(N)]
d = [0] * N
for _ in range(M):
	(U, V) = map(int, input().split())
	G[V - 1].append(U - 1)
	d[U - 1] += 1
dists = [INF] * N
dists[N - 1] = 0
queue = [(0, N - 1)]
while queue:
	(dist, V) = h.heappop(queue)
	if dists[V] < dist:
		continue
	for v in G[V]:
		if dist + d[v] < dists[v]:
			dists[v] = dist + d[v]
			h.heappush(queue, (dist + d[v], v))
		d[v] -= 1
print(dists[0])
