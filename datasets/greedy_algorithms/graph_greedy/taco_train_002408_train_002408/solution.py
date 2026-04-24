import sys
input = sys.stdin.buffer.readline
import heapq
(n, m, k) = map(int, input().split())
k = min(n - 1, k)
graph = [[] for i in range(n)]
edge = {}
for i in range(m):
	(x, y, w) = map(int, input().split())
	edge[x - 1, y - 1] = (w, i)
	edge[y - 1, x - 1] = (w, i)
	graph[x - 1].append(y - 1)
	graph[y - 1].append(x - 1)
ans = []
vis = [0] * n
vis[0] = 1
root = 0
q = []
for i in graph[root]:
	heapq.heappush(q, (edge[i, root][0], root, i))
while len(ans) != k:
	(w, s, e) = heapq.heappop(q)
	if vis[e]:
		continue
	ans.append(edge[s, e][1] + 1)
	vis[e] = 1
	for i in graph[e]:
		if not vis[i]:
			heapq.heappush(q, (w + edge[i, e][0], e, i))
print(len(ans))
print(' '.join(map(str, ans)))
